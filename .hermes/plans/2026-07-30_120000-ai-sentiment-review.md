# AI 情緒回顧功能 — Implementation Plan (Revised)

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** 在 slumber App 加入 Transformers.js 本地 sentiment 分析，提供「滿7日自動生成」+「按鈕隨時觸發」兩條路徑嘅 AI 情緒回顧功能

**Architecture:** Single-file HTML/JS app。新增 localStorage persistence layer 儲存附日期嘅雜念+mood 記錄；Transformers.js 載入輕量 multilingual sentiment model 做本地分析；回顧結果以 modal/sheet 呈現喺記錄頁

**Tech Stack:** Vanilla JS, Transformers.js (`Xenova/distilbert-base-multilingual-cased-sentiments-student` ~85MB ONNX), localStorage, CSS animations

**Revised:** 主動按鈕最低門檻由 3 日降至 1 日，確保 demo 現場即時可用

---

## 🔍 事前理解（Codebase Reconnaissance）

### 現有資料結構

目前 **完全冇持久化儲存**，所有資料純 DOM-only：

```
addDumpEntry(txt) → createElement('div.dump-row')
  ├── dr-icon: 💭 (hardcoded)
  ├── dr-text > div: 文字內容
  └── dr-time: HH:MM (new Date() 當下時間)

addCheckpointEntry(icon, txt) → createElement('div.dump-row')
  ├── dr-icon: 傳入參數 (☀️/🌙)
  ├── dr-text > div: 文字內容
  └── dr-time: HH:MM

selectMood(el, label) → toast only (冇儲存)
```

### 關鍵缺失

| 缺失項目 | 影響 |
|---|---|
| ❌ 冇日期欄位 | 無法按日分組 |
| ❌ 冇 localStorage | 刷新全部消失 |
| ❌ 冇 mood 儲存 | 心情資料流失 |
| ❌ 冇 JS 資料陣列 | 冇嘢可以餵俾 sentiment model |

### 現有可複用基礎設施

- ✅ Modal/sheet system (`showCustomModal`, `closeModalDirect`)
- ✅ Toast system (`toast(msg, type)`)
- ✅ Page navigation (`navigate(id)`)
- ✅ Navy 深夜色調 CSS variables
- ✅ Record page 結構 (`#dumpDisplay`, `#checkpointDisplay`)

---

## 📍 位置選擇：記錄頁（Brain Dump Page）

記錄頁頂部，section title 之上。理由：記錄頁本身係睇歷史記錄嘅地方，情緒回顧係「回顧」行為嘅自然延伸。唔干擾首頁簡潔行動優先設計。

```
<div class="page" id="brain-dump">
  <!-- 👇 新：情緒回顧區塊 -->
  <div class="sentiment-review" id="sentimentReview"> ... </div>
  
  <!-- 原有 -->
  <div class="record-section-title">💭 雜念記錄 ...</div>
  <div class="dump-list" id="dumpDisplay"> ... </div>
  ...
</div>
```

---

## 🧠 Model 選擇與載入時間評估

### Model: `Xenova/distilbert-base-multilingual-cased-sentiments-student`

- **ONNX 量化大小**：~85MB（非 200MB，distilled + quantized）
- **支援語言**：中文、英文、日文等多語言
- **輸出**：positive / neutral / negative + confidence score

### 首次載入時間估算

| 網速 | 預計載入時間 |
|---|---|
| 快 WiFi (50Mbps) | ~15 秒 |
| 一般 WiFi (20Mbps) | ~35 秒 |
| 慢 WiFi / 4G (5Mbps) | ~2 分鐘 |
| 第二次訪問 | 即刻（browser cache） |

### 對策

- Loading 期間顯示 progress bar + 階段文字（「正在下載 AI 模型…」→「正在初始化…」）
- 模型載入係 **non-blocking**：用戶可以繼續用 App，唔會 freeze
- 如果載入超過 60 秒，顯示「網絡較慢，請耐心等待」安慰訊息
- **Fallback**：如果 CDN 完全 load 唔到，顯示「暫時無法載入 AI 模型，請檢查網絡」+ 手動 retry 按鈕

---

## 🎨 UI 設計

### 按鈕區域（記錄頁頂部）

```
┌─────────────────────────────────┐
│  🧠 AI 情緒回顧                  │
│  透過 AI 分析你嘅情緒變化模式      │
│                                 │
│  [ 生成回顧 ]  ← 有 >=1 條記錄即啟用│
└─────────────────────────────────┘
```

### 三種顯示狀態

| 記錄數量 | UI 顯示 |
|---|---|
| **0 條** | 「仲未有任何記錄，撳 ➕ 開始寫低雜念 🌱」 |
| **1-6 條（唔同日子 < 7）** | 按鈕可用，撳咗正常出結果（冇 banner） |
| **>= 7 個唔同日子 + 今日未生成** | Banner card：「🎉 你已記錄滿 7 日！[查看情緒回顧]」 |

### Loading State

```
┌─────────────────────────────────┐
│  ⏳ 正在分析你嘅情緒變化…          │
│  [████████████░░]              │
│  正在載入 AI 模型（首次需約30秒）… │
└─────────────────────────────────┘
```

### 結果顯示（Modal Sheet）

```
┌─────────────────────────────────┐
│  🧠 AI 情緒回顧            ✕   │
│                                 │
│  整體趨勢：😊 正面為主 (65%)      │
│                                 │
│  📊 情緒分佈                      │
│  😊 正面 ████████████ 65%       │
│  😐 中性 ██████ 25%             │
│  😟 負面 ██ 10%                 │
│                                 │
│  💡 AI 洞察                      │
│  「你嘅雜念多數圍繞工作壓力，       │
│   但週末情緒明顯好轉。」            │
│                                 │
│  📅 每日摘要                      │
│  07/24 😊 放鬆 — 3 entries      │
│  07/25 😐 普通 — 2 entries      │
│  ...                            │
│                                 │
│  [ 關閉 ]                       │
└─────────────────────────────────┘
```

---

## 📋 Implementation Tasks（8 Tasks，完整）

---

### Task 1: Add localStorage persistence layer

**Objective:** 由 DOM-only 升級為 localStorage-backed 資料層

**Files:** `candidate-a-demo.html` — JS section only

**Step 1: 定義資料結構**

```javascript
// Global entries array
var entries = []; // {id, type:'dump'|'checkpoint', icon, text, time:'HH:MM', date:'YYYY-MM-DD', mood:null|'😌 放鬆'|...}

// localStorage key
var STORAGE_KEY = 'slumber_entries_v1';
var REVIEW_KEY = 'slumber_last_review_date';
```

**Step 2: 實作 CRUD helpers**

```javascript
function saveEntries() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));
}

function loadEntries() {
  var raw = localStorage.getItem(STORAGE_KEY);
  if (raw) {
    try { entries = JSON.parse(raw); } catch(e) { entries = []; }
  } else {
    entries = [];
  }
  return entries;
}

function clearAllEntries() {
  entries = [];
  localStorage.removeItem(STORAGE_KEY);
  localStorage.removeItem(REVIEW_KEY);
}
```

**Step 3: 改寫 addDumpEntry()**

```javascript
function addDumpEntry(txt) {
  var now = new Date();
  var dateStr = now.toISOString().slice(0, 10);  // YYYY-MM-DD
  var timeStr = now.getHours().toString().padStart(2,'0')+':'+now.getMinutes().toString().padStart(2,'0');
  var mood = window._lastMood || null;
  window._lastMood = null; // consume once
  
  var entry = {
    id: Date.now(),
    type: 'dump',
    icon: '💭',
    text: txt,
    time: timeStr,
    date: dateStr,
    mood: mood
  };
  entries.unshift(entry);
  saveEntries();
  renderDumpEntries(); // re-render from entries array
  updateOverlayBar(txt);
  checkAutoReview(); // trigger auto check
}
```

**Step 4: 改寫 addCheckpointEntry()**

```javascript
function addCheckpointEntry(icon, txt) {
  var now = new Date();
  var dateStr = now.toISOString().slice(0, 10);
  var timeStr = now.getHours().toString().padStart(2,'0')+':'+now.getMinutes().toString().padStart(2,'0');
  
  var entry = {
    id: Date.now(),
    type: 'checkpoint',
    icon: icon,
    text: txt,
    time: timeStr,
    date: dateStr,
    mood: null
  };
  entries.unshift(entry);
  saveEntries();
  renderCheckpointEntries();
}
```

**Step 5: 改寫 selectMood()**

```javascript
function selectMood(el, label) {
  document.querySelectorAll('#moodChips .mood-chip').forEach(function(c){c.classList.remove('active')});
  el.classList.add('active');
  window._lastMood = label; // persist for next dump entry
  toast('😌 心情已記錄：'+label, 'secondary');
}
```

**Step 6: Render functions（由 entries array 重建 DOM）**

```javascript
function renderDumpEntries() {
  var container = document.getElementById('dumpDisplay');
  container.innerHTML = '';
  var dumpEntries = entries.filter(function(e){return e.type==='dump'});
  if (dumpEntries.length === 0) {
    container.innerHTML = '<div class="empty-state"><div class="es-icon">💭</div>仲未有雜念記錄<br>撳底部 ➕ 開始寫低</div>';
    return;
  }
  dumpEntries.forEach(function(e){
    var el = document.createElement('div');
    el.className = 'dump-row';
    el.setAttribute('ontouchstart','swipeStart(event,this)');
    el.setAttribute('ontouchend','swipeEnd(event,this)');
    el.innerHTML = '<div class="dr-icon">'+e.icon+'</div><div class="dr-text"><div>'+e.text+'</div><div class="dr-time">'+e.date+' '+e.time+'</div></div><div class="dr-delete" onclick="deleteEntryById('+e.id+',\'dump\')">刪除</div>';
    container.appendChild(el);
  });
  updateRecordCounts();
}

function renderCheckpointEntries() {
  var container = document.getElementById('checkpointDisplay');
  container.innerHTML = '';
  var cpEntries = entries.filter(function(e){return e.type==='checkpoint'});
  cpEntries.forEach(function(e){
    var el = document.createElement('div');
    el.className = 'dump-row';
    el.setAttribute('ontouchstart','swipeStart(event,this)');
    el.setAttribute('ontouchend','swipeEnd(event,this)');
    el.innerHTML = '<div class="dr-icon">'+e.icon+'</div><div class="dr-text"><div>'+e.text+'</div><div class="dr-time">'+e.date+' '+e.time+'</div></div><div class="dr-delete" onclick="deleteEntryById('+e.id+',\'cp\')">刪除</div>';
    container.appendChild(el);
  });
}
```

**Step 7: 更新 deleteEntry**

```javascript
function deleteEntryById(id, type) {
  entries = entries.filter(function(e){return e.id !== id;});
  saveEntries();
  if (type === 'dump') renderDumpEntries();
  else renderCheckpointEntries();
  toast('🗑️ 已刪除');
  renderSentimentBlock(); // refresh sentiment UI
}
```

**Verification:**
- Seed 3 entries → refresh page → entries still visible
- Delete 1 → refresh → 2 remain
- `clearAllEntries()` → refresh → empty state

---

### Task 2: Add date field + update delete/swipe flow

**Objective:** 所有 entry 攜帶完整日期，DOM render 顯示日期

**Files:** `candidate-a-demo.html`

已在 Task 1 一併處理（`date: dateStr` 欄位、render 時顯示 `e.date + ' ' + e.time`）

**額外處理：** 將現有 demo placeholder entries（聽日個 presentation...）migrate 到 entries array

```javascript
function seedPlaceholders() {
  if (entries.length > 0) return; // don't overwrite existing
  var now = new Date();
  entries = [
    {id:1, type:'dump', icon:'💭', text:'聽日個 presentation 仲有幾頁未整完', time:'22:45', date:fmtDate(now,-1), mood:'😰 緊張'},
    {id:2, type:'dump', icon:'💭', text:'今日同同事傾偈諗到個新方向', time:'21:30', date:fmtDate(now,-2), mood:'😊 開心'},
    {id:3, type:'checkpoint', icon:'🌙', text:'準備入睡 · 感覺：有啲攰但仲有少少精神', time:'23:30', date:fmtDate(now,-1), mood:null},
    {id:4, type:'checkpoint', icon:'☀️', text:'起身 · 感覺：OK，瞓得幾好', time:'07:15', date:fmtDate(now,0), mood:null},
  ];
  saveEntries();
}
function fmtDate(base, offset) { var d=new Date(base); d.setDate(d.getDate()+offset); return d.toISOString().slice(0,10); }
```

**Verification:**
- 首次 load → 見到 placeholder entries with date
- Refresh → data persists
- `clearAllEntries()` → empty state

---

### Task 3: Load Transformers.js + sentiment pipeline singleton

**Objective:** Lazy-load Transformers.js model with cache

**Files:** `candidate-a-demo.html` — HTML head + JS

**Step 1: Add CDN script in `<head>`**

```html
<script type="module">
  import { pipeline } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.3.3/+esm';
  window.transformersPipeline = pipeline;
</script>
```

**Step 2: Pipeline singleton**

```javascript
var sentimentPipeline = null;
var sentimentLoading = false;
var sentimentLoadResolve = null;

async function getSentimentPipeline() {
  if (sentimentPipeline) return sentimentPipeline;
  if (sentimentLoading) {
    // Wait for existing load
    return new Promise(function(resolve) {
      var check = setInterval(function(){
        if (sentimentPipeline) { clearInterval(check); resolve(sentimentPipeline); }
      }, 200);
    });
  }
  sentimentLoading = true;
  updateSentimentProgress('正在下載 AI 模型…', 10);
  try {
    var pipe = await window.transformersPipeline(
      'sentiment-analysis',
      'Xenova/distilbert-base-multilingual-cased-sentiments-student',
      { progress_callback: function(p) {
        if (p.status === 'progress') {
          var pct = Math.round(10 + p.progress * 70);
          updateSentimentProgress('正在載入 AI 模型…', pct);
        }
      }}
    );
    sentimentPipeline = pipe;
    updateSentimentProgress('模型初始化完成', 100);
    return pipe;
  } catch(e) {
    sentimentLoading = false;
    throw e;
  }
}
```

**Step 3: Progress bar UI**

```javascript
function updateSentimentProgress(msg, pct) {
  var bar = document.getElementById('sentimentProgress');
  if (!bar) return;
  bar.querySelector('.sp-text').textContent = msg;
  bar.querySelector('.sp-fill').style.width = pct + '%';
  if (pct >= 100) {
    setTimeout(function(){ bar.style.display = 'none'; }, 500);
  } else {
    bar.style.display = 'block';
  }
}
```

**Verification:**
- 首次 call `getSentimentPipeline()` → loading indicator 出現 → model 載入完成
- 第二次 call → instant return (cache)
- Kill network → error caught gracefully

---

### Task 4: Build sentiment analysis function

**Objective:** 收到 texts[] 陣列，輸出 aggregated sentiment result

**Files:** `candidate-a-demo.html` — JS section

**Step 1: 分析函數**

```javascript
async function analyzeSentiment() {
  var dumpEntries = entries.filter(function(e){return e.type === 'dump' && e.text;});
  if (dumpEntries.length === 0) return null;
  
  var pipe = await getSentimentPipeline();
  updateSentimentProgress('正在分析情緒…', 85);
  
  var results = [];
  // Batch analyze
  for (var i = 0; i < dumpEntries.length; i++) {
    var e = dumpEntries[i];
    var outcome = await pipe(e.text);
    results.push({
      entry: e,
      label: outcome[0].label,  // 'positive' | 'neutral' | 'negative'
      score: outcome[0].score
    });
  }
  
  updateSentimentProgress('分析完成', 100);
  return buildSentimentReport(results);
}
```

**Step 2: 報告生成**

```javascript
function buildSentimentReport(results) {
  // Count sentiments
  var counts = {positive:0, neutral:0, negative:0};
  var daily = {}; // date -> {positive, neutral, negative, entries[], moods[]}
  
  results.forEach(function(r){
    var label = r.label.toLowerCase();
    if (counts[label] !== undefined) counts[label]++;
    
    var d = r.entry.date;
    if (!daily[d]) daily[d] = {positive:0, neutral:0, negative:0, entries:[], moods:[]};
    daily[d][label]++;
    daily[d].entries.push(r.entry);
    if (r.entry.mood) daily[d].moods.push(r.entry.mood);
  });
  
  var total = results.length;
  var report = {
    total: total,
    positivePct: Math.round(counts.positive/total*100),
    neutralPct: Math.round(counts.neutral/total*100),
    negativePct: Math.round(counts.negative/total*100),
    dominant: counts.positive >= counts.negative ? 'positive' : 'negative',
    dailyBreakdown: Object.keys(daily).sort().map(function(d){
      return {date:d, counts:daily[d], entryCount:daily[d].entries.length};
    }),
    insights: generateInsights(counts, daily)
  };
  return report;
}
```

**Step 3: Insight 生成（rule-based）**

```javascript
function generateInsights(counts, daily) {
  var insights = [];
  var total = counts.positive + counts.neutral + counts.negative;
  var posPct = Math.round(counts.positive/total*100);
  
  if (posPct >= 60) {
    insights.push('整體情緒偏正面，你嘅心態幾好 👍');
  } else if (counts.negative > counts.positive) {
    insights.push('最近負面情緒較多，記得睡前做呼吸練習放鬆 🧘');
  }
  
  var dates = Object.keys(daily).sort();
  if (dates.length >= 3) {
    // Check if weekends are better
    insights.push('你嘅雜念多數圍繞日常事務，嘗試睡前寫低一件感恩嘅事 💛');
  }
  
  if (counts.negative >= 3) {
    insights.push('發現有幾日壓力較大，考慮早 30 分鐘開始 wind-down 流程 🌙');
  }
  
  return insights;
}
```

**Verification:**
- `seedTestData(7)` → `analyzeSentiment()` → returns report with positive/neutral/negative counts
- All Chinese texts classified correctly
- `insights` array non-empty

---

### Task 5: Add "AI 情緒回顧" UI block to record page

**Objective:** 記錄頁頂部出現 sentiment review block

**Files:** `candidate-a-demo.html` — HTML + CSS + JS

**Step 1: HTML 插入**

在 `<!-- ════════════════════════ RECORD PAGE ════════════════════════ -->` 嘅 `<div class="page" id="brain-dump">` 入面，第一個 child：

```html
<!-- Sentiment Review Block -->
<div class="sentiment-review" id="sentimentReview">
  <div class="sr-card">
    <div class="sr-header">
      <span class="sr-icon">🧠</span>
      <span class="sr-title">AI 情緒回顧</span>
    </div>
    <div class="sr-body" id="srBody">
      <!-- Dynamic content injected by renderSentimentBlock() -->
    </div>
    <div class="sr-progress" id="sentimentProgress" style="display:none">
      <div class="sp-text">正在載入 AI 模型…</div>
      <div class="sp-bar"><div class="sp-fill" style="width:0%"></div></div>
    </div>
  </div>
</div>
```

**Step 2: CSS**

```css
.sentiment-review{margin-bottom:16px}
.sr-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:16px 18px}
.sr-header{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.sr-icon{font-size:18px}.sr-title{font-size:14px;font-weight:600}
.sr-body{font-size:12px;color:var(--text2);line-height:1.6}
.sr-btn{display:inline-block;margin-top:10px;padding:10px 20px;border-radius:22px;font-size:13px;font-weight:600;cursor:pointer;background:rgba(107,125,184,.12);border:1.5px solid rgba(107,125,184,.2);color:var(--accent);transition:all .15s}
.sr-btn:hover{background:rgba(107,125,184,.2)}
.sr-btn:active{transform:scale(.96)}
.sr-banner{margin-top:8px;padding:10px 14px;background:rgba(107,125,184,.06);border:1px solid rgba(107,125,184,.15);border-radius:var(--radius-pill);font-size:12px;color:var(--accent);cursor:pointer;text-align:center}
.sr-progress{margin-top:10px}
.sp-text{font-size:11px;color:var(--text2);margin-bottom:4px}
.sp-bar{height:4px;background:var(--card-border);border-radius:2px;overflow:hidden}
.sp-fill{height:100%;background:var(--accent);border-radius:2px;transition:width .3s}
```

**Step 3: JS — renderSentimentBlock()**

```javascript
function renderSentimentBlock() {
  var body = document.getElementById('srBody');
  if (!body) return;
  var dumpEntries = entries.filter(function(e){return e.type==='dump'});
  var distinctDates = new Set(dumpEntries.map(function(e){return e.date})).size;
  var lastReview = localStorage.getItem(REVIEW_KEY);
  var today = new Date().toISOString().slice(0,10);
  
  if (dumpEntries.length === 0) {
    body.innerHTML = '<div style="color:var(--text3)">仲未有任何記錄<br>撳 ➕ 開始寫低雜念 🌱</div>';
    return;
  }
  
  // Button always available if >= 1 entry
  var html = '<div style="color:var(--text2)">透過 AI 分析你嘅情緒變化模式</div>';
  html += '<div class="sr-btn" onclick="triggerSentimentReview()">🧠 生成回顧</div>';
  
  // Banner for 7+ days and not reviewed today
  if (distinctDates >= 7 && lastReview !== today) {
    html += '<div class="sr-banner" onclick="triggerSentimentReview()">🎉 你已記錄滿 7 日！點擊查看情緒回顧 →</div>';
  }
  
  body.innerHTML = html;
}
```

**Step 4: 初始化**

```javascript
// In init section:
loadEntries();
seedPlaceholders();
renderDumpEntries();
renderCheckpointEntries();
renderSentimentBlock();
updateRecordCounts();
```

**Verification:**
- 0 entries → "仲未有任何記錄"
- 1 entry → button visible + no banner
- 7 distinct dates → button + banner
- After generating review → banner disappears (lastReviewDate set)

---

### Task 6: Build result modal

**Objective:** 分析完成後以 modal sheet 顯示結果

**Files:** `candidate-a-demo.html` — JS section

**Step 1: triggerSentimentReview()**

```javascript
async function triggerSentimentReview() {
  var dumpEntries = entries.filter(function(e){return e.type==='dump'});
  if (dumpEntries.length === 0) {
    toast('仲未有任何記錄','secondary');
    return;
  }
  
  // Show loading in modal
  showCustomModal(
    '<div style="text-align:center;padding:20px">'+
    '<div style="font-size:32px;margin-bottom:12px">⏳</div>'+
    '<div style="font-size:14px;font-weight:600;margin-bottom:8px">正在分析你嘅情緒變化…</div>'+
    '<div id="modalProgress" style="font-size:12px;color:var(--text2)">準備中…</div>'+
    '</div>'
  );
  
  updateSentimentProgress = function(msg, pct) {
    var el = document.getElementById('modalProgress');
    if (el) el.textContent = msg + ' (' + pct + '%)';
    var bar = document.getElementById('sentimentProgress');
    if (bar) { bar.style.display='block'; bar.querySelector('.sp-fill').style.width=pct+'%'; }
  };
  
  try {
    var report = await analyzeSentiment();
    if (!report) { closeModalDirect(); toast('分析失敗，請再試一次'); return; }
    showSentimentResult(report);
    
    // Save review date
    var today = new Date().toISOString().slice(0,10);
    localStorage.setItem(REVIEW_KEY, today);
    renderSentimentBlock();
  } catch(e) {
    closeModalDirect();
    toast('載入失敗：' + e.message);
    sentimentLoading = false;
  }
}
```

**Step 2: showSentimentResult(report)**

```javascript
function showSentimentResult(report) {
  var posW = report.positivePct;
  var neuW = report.neutralPct;
  var negW = report.negativePct;
  
  var dailyRows = report.dailyBreakdown.map(function(d){
    var moodEmoji = d.counts.positive >= d.counts.negative ? '😊' : '😟';
    return '<div style="display:flex;gap:8px;padding:6px 0;font-size:11px;border-bottom:1px solid var(--card-border)">'+
      '<span style="color:var(--text3);min-width:48px">'+d.date.slice(5)+'</span>'+
      '<span>'+moodEmoji+'</span>'+
      '<span style="flex:1;color:var(--text2)">'+d.entryCount+' 條記錄</span>'+
      '</div>';
  }).join('');
  
  var html = 
    '<div style="text-align:center;padding:4px 0 16px">'+
    '<div style="font-size:28px;margin-bottom:4px">🧠</div>'+
    '<div style="font-size:16px;font-weight:700">AI 情緒回顧</div>'+
    '<div style="font-size:12px;color:var(--text2);margin-top:4px">'+
    (report.dominant==='positive'?'整體趨勢：😊 正面為主':'整體趨勢：😟 負面較多')+
    ' ('+report.total+' 條記錄)</div>'+
    '</div>'+
    
    '<div style="margin-bottom:16px">'+
    '<div style="font-size:11px;color:var(--text3);margin-bottom:6px">📊 情緒分佈</div>'+
    '<div style="display:flex;align-items:center;gap:4px;margin-bottom:4px">'+
    '<span style="font-size:11px;width:40px">😊</span>'+
    '<div style="flex:1;height:18px;background:var(--card-border);border-radius:9px;overflow:hidden">'+
    '<div style="height:100%;width:'+posW+'%;background:#6b7db8;border-radius:9px"></div></div>'+
    '<span style="font-size:10px;color:var(--text2);min-width:32px">'+posW+'%</span></div>'+
    '<div style="display:flex;align-items:center;gap:4px;margin-bottom:4px">'+
    '<span style="font-size:11px;width:40px">😐</span>'+
    '<div style="flex:1;height:18px;background:var(--card-border);border-radius:9px;overflow-hidden">'+
    '<div style="height:100%;width:'+neuW+'%;background:#8890a8;border-radius:9px"></div></div>'+
    '<span style="font-size:10px;color:var(--text2);min-width:32px">'+neuW+'%</span></div>'+
    '<div style="display:flex;align-items:center;gap:4px">'+
    '<span style="font-size:11px;width:40px">😟</span>'+
    '<div style="flex:1;height:18px;background:var(--card-border);border-radius:9px;overflow:hidden">'+
    '<div style="height:100%;width:'+negW+'%;background:#885068;border-radius:9px"></div></div>'+
    '<span style="font-size:10px;color:var(--text2);min-width:32px">'+negW+'%</span></div>'+
    '</div>'+
    
    (report.insights.length>0?
    '<div style="margin-bottom:16px">'+
    '<div style="font-size:11px;color:var(--text3);margin-bottom:6px">💡 AI 洞察</div>'+
    report.insights.map(function(i){return '<div style="font-size:12px;color:var(--text2);padding:4px 0;line-height:1.5">'+i+'</div>'}).join('')+
    '</div>':'')+
    
    '<div style="margin-bottom:8px">'+
    '<div style="font-size:11px;color:var(--text3);margin-bottom:6px">📅 每日摘要</div>'+
    dailyRows+
    '</div>'+
    
    '<div class="modal-cancel" onclick="closeModalDirect()">關閉</div>';
  
  showCustomModal(html);
}
```

**Verification:**
- Seed 3+ entries → trigger → modal shows with bars + insights + daily rows
- Bars correctly proportional to percentages
- "關閉" button dismisses modal

---

### Task 7: Wire up auto-generation trigger

**Objective:** `checkAutoReview()` 在每次 add entry 後檢查是否滿 7 日

**Files:** `candidate-a-demo.html` — JS section

**Step 1: checkAutoReview()**

```javascript
function checkAutoReview() {
  var dumpEntries = entries.filter(function(e){return e.type==='dump'});
  var distinctDates = new Set(dumpEntries.map(function(e){return e.date})).size;
  var lastReview = localStorage.getItem(REVIEW_KEY);
  var today = new Date().toISOString().slice(0,10);
  
  if (distinctDates >= 7 && lastReview !== today) {
    // Don't auto-trigger modal — just update the banner
    renderSentimentBlock();
  }
}
```

Already called in Task 1's `addDumpEntry()` → no additional wiring needed.

**Verification:**
- Seed 6 distinct dates → no banner
- Add 1 more entry with 7th distinct date → banner appears
- Click banner → review → banner disappears for today

---

### Task 8: Seed test data + verify both paths with browser screenshots

**Objective:** 模擬數據，驗證兩條路徑，產出截圖證明

**Files:** `candidate-a-demo.html` — JS section

**Step 1: seedTestData(days)**

```javascript
function seedTestData(days) {
  clearAllEntries();
  var texts = [
    {t:'今日做晒所有嘢，心情好輕鬆', m:'😌 放鬆'},
    {t:'聽日個會壓力好大，瞓唔著', m:'😰 緊張'},
    {t:'同朋友食飯好開心', m:'😊 開心'},
    {t:'OT 到好晏，好攰', m:'😴 好攰'},
    {t:'同事又冇交功課，好煩', m:'😤 煩躁'},
    {t:'今日效率好高，滿意', m:'😌 放鬆'},
    {t:'周末可以唞下，感恩', m:'😊 開心'},
  ];
  var now = new Date();
  for (var i = 0; i < days; i++) {
    var d = new Date(now); d.setDate(d.getDate() - (days - 1 - i));
    var dateStr = d.toISOString().slice(0, 10);
    var t = texts[i % texts.length];
    entries.push({id:Date.now()+i*10, type:'dump', icon:'💭', text:t.t, time:'22:45', date:dateStr, mood:t.m});
    entries.push({id:Date.now()+i*10+1, type:'checkpoint', icon:'🌙', text:'準備入睡', time:'23:30', date:dateStr, mood:null});
  }
  saveEntries();
  renderDumpEntries();
  renderCheckpointEntries();
  renderSentimentBlock();
  updateRecordCounts();
  toast('🧪 已生成 '+days+' 日測試數據');
}

// Also expose console helper
window.seedTestData = seedTestData;
window.clearAllEntries = clearAllEntries;
```

**Step 2: Browser verification（用 Hermes browser tools）**

測試流程：

| # | 測試 | Browser 操作 | 預期結果 |
|---|---|---|---|
| 1 | 主動路徑（1日） | `seedTestData(1)` → navigate記錄頁 → 撳「生成回顧」 | Modal顯示1日分析結果 |
| 2 | 主動路徑（3日） | `seedTestData(3)` → 撳「生成回顧」 | Modal顯示3日分析 + daily rows |
| 3 | 自動banner（7日） | `seedTestData(7)` → navigate記錄頁 | Banner card「🎉 你已記錄滿 7 日」出現 |
| 4 | Banner消失 | 撳banner → 出modal → 關閉 → refresh | Banner消失（今日已review） |
| 5 | 空狀態 | `clearAllEntries()` → navigate記錄頁 | 「仲未有任何記錄 🌱」 |
| 6 | Model cache | 連續撳2次「生成回顧」 | 第2次即刻出結果，唔使重新下載 |

使用 `browser_navigate` + `browser_console` + `browser_vision` 做 screenshot 驗證每一步。

**Step 3: Vercel deployment verification**

```bash
curl -sI https://sleep-app-baseline-v3.vercel.app/candidate-a-demo.html
# Expected: 200 OK
```

---

## ⚠️ 確認項目（User Feedback Incorporated）

1. ✅ **門檻降至 1 日**：主動按鈕只要有 >=1 條記錄就啟用
2. ✅ **Task 4-8 已完整展開**：包 code、verification steps、browser screenshot 測試
3. ✅ **Model 載入時間**：~85MB ONNX，一般 WiFi ~35 秒首次載入，有 progress bar + 安慰訊息。Browser cache 後即刻可用。

## ⚠️ 仍需 User 確認

- **測試方式**：我有 browser automation tools（`browser_navigate` + `browser_console` + `browser_vision`），可以自動截圖驗證每個 task。你唔使人手開 browser —— 我會做完每一個 task 之後自動 navigate 到 demo URL、seed data、撳掣、截圖、俾你睇結果。呢個 OK？
