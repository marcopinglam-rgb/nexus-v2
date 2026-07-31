# Unified Zero-Shot AI Classification Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Replace the existing fixed-label sentiment model with a single `Xenova/mDeBERTa-v3-base-xnli` zero-shot pipeline that performs **both** sentiment analysis (3 labels) AND brain-dump category classification (4 labels) in one `multi_label` call, then display inline category badges on each dump entry row.

**Architecture:** One model, one load, one pipeline call per entry with 7 Chinese labels. Results are split into a `sentiment` group (正面情緒/中性情緒/負面情緒) and a `category` group (今日任務/未解決煩惱/隨手靈感/情緒宣洩). The pipeline singleton and progress callback pattern from the old `sentimentPipeline` are reused.

**Tech Stack:** Transformers.js 3.3.3 (CDN), zero-shot-classification pipeline, localStorage

---

## Impact Summary

| | Before | After |
|---|---|---|
| CDN import | `sentiment-analysis` | `zero-shot-classification` (same import call, different pipeline type) |
| Model | `Xenova/distilbert-base-multilingual-cased-sentiments-student` (~250MB) | `Xenova/mDeBERTa-v3-base-xnli` (~1.1GB) |
| Pipeline singleton | `sentimentPipeline` | `zeroShotPipeline` |
| entries[] fields | `id, type, icon, text, time, date, mood` | **+ `category`** (String \| null) |
| `analyzeSentiment()` | fixed-label per entry | zero-shot multi_label per entry, then split |
| Storage key | `slumber_entries_v1` | **`slumber_entries_v2`** (schema migration) |

---

## Task Breakdown

### Task 1: Change CDN import & model

**Objective:** Swap the Transformers.js pipeline type and model name.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:8`

**Step 1: Replace the `<script type="module">` import**

Old:
```html
<script type="module">
  import { pipeline } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.3.3/+esm';
  window.transformersPipeline = pipeline;
</script>
```

New (unchanged — the `pipeline` function is the same, just the calling code changes):

No change needed here. The `pipeline` import is generic — it works for both `sentiment-analysis` and `zero-shot-classification`. ✅

**Step 2: No file change needed for Task 1.** The pipeline function handles both types.

**Verification:** Nothing to verify yet — proves itself in Task 3.

---

### Task 2: Replace pipeline singleton + add label constants

**Objective:** Replace `sentimentPipeline`/`sentimentLoading` with `zeroShotPipeline`/`zeroShotLoading`, add the 7-label array, and rewrite `getSentimentPipeline()` → `getZeroShotPipeline()`.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:552` (state vars)
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:923-931` (getSentimentPipeline)
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:552` (add label constants)

**Step 1: Change state variables**

Find line 552:
```js
var sentimentPipeline=null,sentimentLoading=false;
```

Replace with:
```js
var zeroShotPipeline=null,zeroShotLoading=false;
var ZS_LABELS=['正面情緒','中性情緒','負面情緒','今日任務','未解決煩惱','隨手靈感','情緒宣洩'];
var SENTIMENT_LABELS=ZS_LABELS.slice(0,3);
var CATEGORY_LABELS=ZS_LABELS.slice(3,7);
```

**Step 2: Rewrite `getSentimentPipeline()` → `getZeroShotPipeline()`**

Find the function at line 923:
```js
async function getSentimentPipeline(){
  if(sentimentPipeline)return sentimentPipeline;
  if(sentimentLoading){return new Promise(function(r){var c=setInterval(function(){if(sentimentPipeline){clearInterval(c);r(sentimentPipeline);}},200);});}
  sentimentLoading=true;updateSentimentProgress('正在下載 AI 模型…',10);
  try{
    var pipe=await window.transformersPipeline('sentiment-analysis','Xenova/distilbert-base-multilingual-cased-sentiments-student',{progress_callback:function(p){if(p.status==='progress'){var pct=Math.round(10+p.progress*70);updateSentimentProgress('正在載入 AI 模型…',pct);}}});
    sentimentPipeline=pipe;updateSentimentProgress('模型初始化完成',100);return pipe;
  }catch(e){sentimentLoading=false;throw e;}
}
```

Replace with:
```js
async function getZeroShotPipeline(){
  if(zeroShotPipeline)return zeroShotPipeline;
  if(zeroShotLoading){return new Promise(function(r){var c=setInterval(function(){if(zeroShotPipeline){clearInterval(c);r(zeroShotPipeline);}},200);});}
  zeroShotLoading=true;updateSentimentProgress('正在下載 AI 模型 (zero-shot)…',10);
  try{
    var pipe=await window.transformersPipeline('zero-shot-classification','Xenova/mDeBERTa-v3-base-xnli',{progress_callback:function(p){if(p.status==='progress'){var pct=Math.round(10+p.progress*70);updateSentimentProgress('正在載入 AI 模型…',pct);}}});
    zeroShotPipeline=pipe;updateSentimentProgress('模型初始化完成',100);return pipe;
  }catch(e){zeroShotLoading=false;throw e;}
}
```

**Step 3: Update `triggerSentimentReview()` error handler**

Line 974 references `sentimentLoading=false`. Change to:
```js
}catch(e){if(res)res.style.display='none';toast('載入失敗：'+e.message);zeroShotLoading=false;}
```

**Step 4: Search for any remaining references to `sentimentPipeline` or `sentimentLoading`**

Run: `search_files("sentimentPipeline|sentimentLoading", path="sleep-app-baseline-v3/candidate-a-demo.html")`
Expected: 0 results after all tasks complete.

**Verification:** No syntax errors. The old variable names are gone.

---

### Task 3: Create `classifyEntry(text)` function

**Objective:** Add a function that calls the zero-shot pipeline with all 7 labels in one multi_label call, then splits the result into `{sentiment, category}`.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html` — insert before `analyzeSentiment()`

**Step 1: Insert new function before `analyzeSentiment()` (before line 932)**

```js
async function classifyEntry(text){
  var pipe=await getZeroShotPipeline();
  var result=await pipe(text,ZS_LABELS,{multi_label:true});
  // result: {labels:[...], scores:[...]}
  var bestSentiment=SENTIMENT_LABELS.reduce(function(best,label){
    var idx=result.labels.indexOf(label);
    var score=idx>=0?result.scores[idx]:0;
    return score>best.score?{label:label,score:score}:best;
  },{label:'中性情緒',score:0});
  var bestCategory=CATEGORY_LABELS.reduce(function(best,label){
    var idx=result.labels.indexOf(label);
    var score=idx>=0?result.scores[idx]:0;
    return score>best.score?{label:label,score:score}:best;
  },{label:'隨手靈感',score:0});
  return {
    allLabels:result.labels,
    allScores:result.scores,
    sentiment:bestSentiment.label,
    sentimentScore:bestSentiment.score,
    category:bestCategory.label,
    categoryScore:bestCategory.score
  };
}
```

**Verification:** Function compiles without syntax error.

---

### Task 4: Add `category` field to `entries[]` — `addDumpEntry()` and `seedPlaceholders()`

**Objective:** When a user submits a dump entry, run `classifyEntry()` and store the `category` result. Update seed data too.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:652-665` (`addDumpEntry`)
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:564-574` (`seedPlaceholders`)

**Step 1: Make `addDumpEntry()` async and add classification**

Old (line 652):
```js
function addDumpEntry(txt){
  var now=new Date();
  var dateStr=now.toISOString().slice(0,10);
  var timeStr=now.getHours().toString().padStart(2,'0')+':'+now.getMinutes().toString().padStart(2,'0');
  var mood=window._lastMood||null;window._lastMood=null;
  var entry={id:Date.now(),type:'dump',icon:'💭',text:txt,time:timeStr,date:dateStr,mood:mood};
  entries.unshift(entry);saveEntries();
  renderDumpEntries();
  hasContent=true;
  document.getElementById('barText').textContent=txt;
  document.getElementById('barHint').style.display='none';
  document.getElementById('overlayBar').classList.add('has-content');
  checkAutoReview();
}
```

Replace with:
```js
async function addDumpEntry(txt){
  var now=new Date();
  var dateStr=now.toISOString().slice(0,10);
  var timeStr=now.getHours().toString().padStart(2,'0')+':'+now.getMinutes().toString().padStart(2,'0');
  var mood=window._lastMood||null;window._lastMood=null;
  var entry={id:Date.now(),type:'dump',icon:'💭',text:txt,time:timeStr,date:dateStr,mood:mood,category:null};
  // Async classify — don't block UI rendering
  classifyAndAttach(entry);
  entries.unshift(entry);saveEntries();
  renderDumpEntries();
  hasContent=true;
  document.getElementById('barText').textContent=txt;
  document.getElementById('barHint').style.display='none';
  document.getElementById('overlayBar').classList.add('has-content');
  checkAutoReview();
}
```

**Step 2: Add `classifyAndAttach()` helper (insert before `addDumpEntry`)**

```js
async function classifyAndAttach(entry){
  if(entry.type!=='dump')return;
  try{
    var cls=await classifyEntry(entry.text);
    entry.category=cls.category;
    entry.sentimentLabel=cls.sentiment;
    saveEntries();
    renderDumpEntries();
    updateRecordCounts();
  }catch(e){
    // Classification failed silently — category stays null (graceful degradation)
    console.warn('Auto-classify failed for entry',entry.id,e);
  }
}
```

**Step 3: Update `seedPlaceholders()` (line 567)**

Add `category` and `sentimentLabel` to each seed entry:
```js
entries=[
  {id:1,type:'dump',icon:'💭',text:'聽日個 presentation 仲有幾頁未整完',time:'22:45',date:fmtDate(now,-1),mood:'😰 緊張',category:'今日任務',sentimentLabel:'負面情緒'},
  {id:2,type:'dump',icon:'💭',text:'今日同同事傾偈諗到個新方向',time:'21:30',date:fmtDate(now,-2),mood:'😊 開心',category:'隨手靈感',sentimentLabel:'正面情緒'},
  {id:3,type:'checkpoint',icon:'🌙',text:'準備入睡 · 感覺：有啲攰但仲有少少精神',time:'23:30',date:fmtDate(now,-1),mood:null,category:null},
  {id:4,type:'checkpoint',icon:'☀️',text:'起身 · 感覺：OK，瞓得幾好',time:'07:15',date:fmtDate(now,0),mood:null,category:null},
];
```

**Verification:** Start the app fresh (clear localStorage), verify seed entries show category badges.

---

### Task 5: Storage migration (v1 → v2)

**Objective:** Old entries without `category` still work. Add migration logic on load.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:550` (STORAGE_KEY)
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:557-561` (loadEntries)

**Step 1: Bump storage key**

Line 550:
```js
var STORAGE_KEY='slumber_entries_v1',REVIEW_KEY='slumber_last_review',REVIEW_HISTORY_KEY='slumber_review_history';
```

Change to:
```js
var STORAGE_KEY='slumber_entries_v2',REVIEW_KEY='slumber_last_review',REVIEW_HISTORY_KEY='slumber_review_history';
```

**Step 2: Add migration in `loadEntries()`**

Old (line 557):
```js
function loadEntries(){
  var raw=localStorage.getItem(STORAGE_KEY);
  if(raw){try{entries=JSON.parse(raw);}catch(e){entries=[];}}
  return entries;
}
```

Replace with:
```js
function loadEntries(){
  var raw=localStorage.getItem('slumber_entries_v2');
  if(!raw){
    // Migrate from v1
    var oldRaw=localStorage.getItem('slumber_entries_v1');
    if(oldRaw){try{entries=JSON.parse(oldRaw);entries.forEach(function(e){if(!e.hasOwnProperty('category')){e.category=null;}});saveEntries();}catch(e){entries=[];}}
  }else{
    try{entries=JSON.parse(raw);entries.forEach(function(e){if(!e.hasOwnProperty('category')){e.category=null;}});}catch(e){entries=[];}
  }
  return entries;
}
```

**Verification:** Old `slumber_entries_v1` data loads correctly with `category: null` fallback.

---

### Task 6: Rewrite `analyzeSentiment()` to use zero-shot results

**Objective:** Instead of running fixed-label sentiment per entry, use `classifyEntry()` (which already runs zero-shot) and build the report from those results.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:932-939` (`analyzeSentiment`)

**Step 1: Replace `analyzeSentiment()`**

Old:
```js
async function analyzeSentiment(){
  var dumps=entries.filter(function(e){return e.type==='dump'&&e.text;});
  if(dumps.length===0)return null;
  var pipe=await getSentimentPipeline();updateSentimentProgress('正在分析情緒…',85);
  var results=[];
  for(var i=0;i<dumps.length;i++){var e=dumps[i];var o=await pipe(e.text);results.push({entry:e,label:o[0].label,score:o[0].score});}
  updateSentimentProgress('分析完成',100);return buildSentimentReport(results);
}
```

Replace with:
```js
async function analyzeSentiment(){
  var dumps=entries.filter(function(e){return e.type==='dump'&&e.text;});
  if(dumps.length===0)return null;
  updateSentimentProgress('正在分析情緒…',85);
  var results=[];
  for(var i=0;i<dumps.length;i++){
    var e=dumps[i];
    var cls=await classifyEntry(e.text);
    results.push({entry:e,label:cls.sentiment,score:cls.sentimentScore,category:cls.category,categoryScore:cls.categoryScore});
    // Update the entry in-place so future renders pick up the classification
    e.sentimentLabel=cls.sentiment;
    e.category=cls.category;
  }
  saveEntries(); // persist updated categories
  updateSentimentProgress('分析完成',100);
  return buildSentimentReport(results);
}
```

**Step 2: Update `buildSentimentReport()` to use new result shape**

Line 940 — the function reads `r.label.toLowerCase()` which now returns Chinese labels like `正面情緒`. Replace the mapping:

Old (line 941-954):
```js
function buildSentimentReport(results){
  var counts={positive:0,neutral:0,negative:0};
  var daily={};
  results.forEach(function(r){
    var l=r.label.toLowerCase();if(counts[l]!==undefined)counts[l]++;
    var d=r.entry.date;if(!daily[d])daily[d]={positive:0,neutral:0,negative:0,entries:[],moods:[]};
    daily[d][l]++;daily[d].entries.push(r.entry);if(r.entry.mood)daily[d].moods.push(r.entry.mood);
  });
  var total=results.length;
  return {
    total:total,positivePct:Math.round(counts.positive/total*100),neutralPct:Math.round(counts.neutral/total*100),negativePct:Math.round(counts.negative/total*100),
    dominant:counts.positive>=counts.negative?'positive':'negative',
    dailyBreakdown:Object.keys(daily).sort().map(function(d){return{date:d,counts:daily[d],entryCount:daily[d].entries.length};})
  };
}
```

Replace with:
```js
function buildSentimentReport(results){
  var LABEL_MAP={'正面情緒':'positive','中性情緒':'neutral','負面情緒':'negative'};
  var REV_LABEL_MAP={positive:'正面情緒',neutral:'中性情緒',negative:'負面情緒'};
  var counts={positive:0,neutral:0,negative:0};
  var catCounts={'今日任務':0,'未解決煩惱':0,'隨手靈感':0,'情緒宣洩':0};
  var daily={};
  results.forEach(function(r){
    var key=LABEL_MAP[r.label]||'neutral';counts[key]++;
    if(r.category)catCounts[r.category]=(catCounts[r.category]||0)+1;
    var d=r.entry.date;if(!daily[d])daily[d]={positive:0,neutral:0,negative:0,entries:[],moods:[]};
    daily[d][key]++;daily[d].entries.push(r.entry);if(r.entry.mood)daily[d].moods.push(r.entry.mood);
  });
  var total=results.length;
  return {
    total:total,positivePct:Math.round(counts.positive/total*100),neutralPct:Math.round(counts.neutral/total*100),negativePct:Math.round(counts.negative/total*100),
    dominant:counts.positive>=counts.negative?'positive':'negative',
    categoryCounts:catCounts,
    dailyBreakdown:Object.keys(daily).sort().map(function(d){return{date:d,counts:daily[d],entryCount:daily[d].entries.length};})
  };
}
```

**Step 3: Update `triggerSentimentReview()` narrative generation**

Line 965 — old call passes dummy labels:
```js
report.narrative=generateNarrative(counts,dailyMap,dumps.map(function(){return{label:report.dominant};}));
```

Replace with real labels:
```js
report.narrative=generateNarrative(counts,dailyMap,dumps.map(function(e){return{label:e.sentimentLabel||'中性情緒'};}));
```

**Verification:** Generate a review with test data — verify sentiment bars show correct percentages.

---

### Task 7: Render category badge in `renderDumpEntries()`

**Objective:** Each dump entry row shows a color-coded category pill like `#今日任務`.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:704-714` (`renderDumpEntries`)

**Step 1: Update the render function**

Old (line 708-713):
```js
dumps.forEach(function(e){
  var el=document.createElement('div');el.className='dump-row';
  el.setAttribute('ontouchstart','swipeStart(event,this)');el.setAttribute('ontouchend','swipeEnd(event,this)');
  el.innerHTML='<div class="dr-icon">'+e.icon+'</div><div class="dr-text"><div>'+e.text+'</div><div class="dr-time">'+e.date+' '+e.time+'</div></div><div class="dr-delete" onclick="deleteEntryById('+e.id+',&apos;dump&apos;)">刪除</div>';
  c.appendChild(el);
});updateRecordCounts();
```

Replace with:
```js
dumps.forEach(function(e){
  var el=document.createElement('div');el.className='dump-row';
  el.setAttribute('ontouchstart','swipeStart(event,this)');el.setAttribute('ontouchend','swipeEnd(event,this)');
  var catBadge=e.category?'<span class=\"dr-cat cat-'+categoryCSSClass(e.category)+'\">#'+e.category+'</span>':'';
  var moodTag=e.mood?'<span class=\"dr-mood\">'+e.mood+'</span>':'';
  el.innerHTML='<div class=\"dr-icon\">'+e.icon+'</div><div class=\"dr-text\"><div>'+e.text+' '+catBadge+'</div><div class=\"dr-time\">'+e.date+' '+e.time+' '+moodTag+'</div></div><div class=\"dr-delete\" onclick=\"deleteEntryById('+e.id+',&apos;dump&apos;)">刪除</div>';
  c.appendChild(el);
});updateRecordCounts();
```

**Step 2: Add `categoryCSSClass()` helper**

Insert before `renderDumpEntries`:
```js
function categoryCSSClass(cat){
  var map={'今日任務':'task','未解決煩惱':'worry','隨手靈感':'idea','情緒宣洩':'vent'};
  return map[cat]||'other';
}
```

**Verification:** After seed data loads, each dump row shows a category badge.

---

### Task 8: CSS for category badges + mood tag

**Objective:** Style the `.dr-cat` pills (4 colors) and `.dr-mood` tag.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html` — CSS section (around line 147-158, near `.dump-row` styles)

**Step 1: Add new CSS rules after line 158** (after `.record-section-title`)

Insert:
```css
.dr-cat{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:600;margin-left:6px;vertical-align:middle;white-space:nowrap}
.cat-task{background:rgba(107,125,184,.15);color:#8a9fd4}
.cat-worry{background:rgba(255,140,100,.12);color:#ffa888}
.cat-idea{background:rgba(100,200,160,.12);color:#80d4b8}
.cat-vent{background:rgba(200,140,200,.12);color:#d0a0d0}
.cat-other{background:var(--card-border);color:var(--text3)}
.dr-mood{font-size:10px;color:var(--text3);margin-left:6px}
```

**Verification:** Refresh the page — each dump row has a colored category badge and mood tag.

---

### Task 9: Update `seedTestData()` for testing

**Objective:** `seedTestData()` should include `category` and `sentimentLabel`.

**Files:**
- Modify: `sleep-app-baseline-v3/candidate-a-demo.html:1074-1081`

**Step 1: Update the seed loop**

Old (line 1078):
```js
entries.push({id:Date.now()+i*10,type:'dump',icon:'💭',text:t.t,time:'22:45',date:ds,mood:t.m});entries.push({id:Date.now()+i*10+1,type:'checkpoint',icon:'🌙',text:'準備入睡',time:'23:30',date:ds,mood:null});
```

Replace with:
```js
entries.push({id:Date.now()+i*10,type:'dump',icon:'💭',text:t.t,time:'22:45',date:ds,mood:t.m,category:null,sentimentLabel:null});
entries.push({id:Date.now()+i*10+1,type:'checkpoint',icon:'🌙',text:'準備入睡',time:'23:30',date:ds,mood:null,category:null});
```

**Verification:** Run `seedTestData(7)` in console → 7 days of data → trigger review.

---

### Task 10: Final integration test

**Objective:** Full end-to-end verification.

**Verification steps:**

1. **Clear localStorage** → reload page
2. **Seed data loads** → 4 entries visible with category badges on dump rows
3. **Submit a new dump** via composer bar → entry appears, then category badge populates async
4. **Trigger AI review** → loading bar shows model download progress → review result displays with sentiment bars + narrative
5. **Check history** → tap "📋 歷史回顧" → see saved review in modal
6. **Verify old v1 migration** → manually set `localStorage.setItem('slumber_entries_v1', '[{"id":1,"type":"dump","text":"test"}]')` → reload → entry loads with `category: null` and no crash
7. **Console error check** → no uncaught errors

Run commands:
```bash
# No build step — open in browser directly
# Open: sleep-app-baseline-v3/candidate-a-demo.html
```

**Expected:** All 7 steps pass.

---

## Risks

| Risk | Mitigation |
|---|---|
| mDeBERTa-v3-base-xnli 1.1GB download takes 40s+ on slow network | Acceptable for demo — progress bar gives visibility |
| multi_label zero-shot 7 labels may produce noise | Test with real Cantonese dump text; tune label wording if needed |
| `classifyAndAttach()` async callback may overwrite user edits before render | Classification is read-only on the entry object; UI re-renders atomically |
| Old v1 storage key still has data | Migration step copies + upgrades to v2 key |
