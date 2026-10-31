# NEXUS 交接 — 技術棧摘要 + 已知 Issues（俾 Cursor Pro）

> 追加：2026-10-31。附於 NEXUS_HANDOFF.md 之後。

---

## 1. 技術棧摘要（Tech Stack）

| 層面 | 用咗咩 | 備註 |
|------|--------|------|
| **語言** | 純 HTML / CSS / Vanilla JS（ES6） | 無 TypeScript、無 framework、無 build step |
| **App 結構** | 單頁 PWA `index.html`（454行）+ `app.js`（1212行）+ `styles.css`（365行） | 3 大主檔，無 module 拆分 |
| **離線** | Service Worker `sw.js`（106行）+ `manifest.webmanifest` | 可加主畫面做 standalone |
| **資料儲存** | 純 `localStorage`（key `nexusOS`）| 單機數據，無後端、無帳戶 |
| **AI 功能** | **Mock**（keyword-regex 配對 + i18n 範稿 `ai.reply*`）| ⚠️ 見 Issue #1 |
| **外部依賴** | 淨係 CDN `marked.min.js`（jsdelivr，Markdown 渲染）| 唯一 runtime 依賴 |
| **i18n** | 內建 `i18n` 字典（en / zh-Hant）| 字串全放 i18n，冇硬編碼 |
| **Icon** | outline SVG（`assets/icon.svg`）| 統一風格 |
| **部署** | Vercel static（`vercel.json`：`framework:null`＋`outputDirectory:"."`）| auto-deploy from Git 已確認 work |
| **版本控制** | Git / GitHub（`marcopinglam-rgb/*`）| main branch |
| **設計/system** | 純手寫 CSS（CSS variables + flex/grid）| 無 Tailwind/UI kit |

**原則**（源自 AGENTS.md）：手機-first、底部 tab 導航、觸控目標 ≥44-48px、無依賴 framework、單欄少滾動、PWA standalone。

---

## 2. 已知 Issue List（Known Issues）

### 🔴 功能性 / 需要決定

| # | Issue | 現狀 | 建議 |
|---|-------|------|------|
| **1** | **AI Copilot 係假嘅**：`runAgent()` 淨係 keyword 配對 + 回覆 i18n 範稿，冇真正嘅 LLM/API 呼叫。UI 有 `openAI()` panel 但背後冇 intelligence | 已確認（app.js:939-960）| 決定想唔想要真 AI？想要就接 provider（要 API key + `vercel.json` env），唔想就保持 mock 或標明「demo」 |
| **2** | **無後端 + 無帳戶**：數據全部喺裝置 `localStorage`，換機/清 cache 會無咗所有 dump 同 canvas | by design | 確認係咪要保持單機，定要 sync（要諗 backend） |

### 🟡 剷走技術債（清啲）

| # | Issue | 現狀 |
|---|-------|------|
| **3** | 單一巨型 `app.js`（1212行）+ `index.html`（454行），冇 module 拆分 | 難維護、難加功能 |
| **4** | `assets/icon.svg` 得一個，冇 apple-touch-icon PNG；部分 iOS 裝置可能唔顯示 icon | minor |
| **5** | i18n 有 en + zh-Hant 兩套，但 README 講「粵語 UI」係「本地化方向」（roadmap Should-Have），目前 UI 主語言其實係繁體中文/英文混合 | 確認 target 語言 |

### 🟢 PWA/快取注意（已知會踩）

| # | Issue |
|---|-------|
| **6** | **SW 快取陷阱**：`sw.js` 同 `manifest` 已經喺 `vercel.json` 做咗 `Cache-Control: max-age=0, must-revalidate` ✅。但**改 code 後要確認 SW 版本號有 bump**，否則舊 SW 會 server ー直食住舊版 app 唔更新（PWA 升級唔生效）。check 每次改版有冇加 `CACHE_VERSION`/`version` |

### 🔵 設計約束（唔係 bug，但改 UI 前必讀）
- 睇 `iteration_log.md`：最高分做法 overlay bar(v51)=4.76、thumb zone+cotenter plus(v30)=4.72 — 改 layout 前跟住呢啲驗證過嘅 pattern，唔好由零諗
- 「AI Future Leader」比賽 context，`IDEA.md` 講明人定方向、AI 執行

---

## 3. 點樣俾個 repo path Cursor Pro

兩個 repo 都係 **public**，所以 Cursor 唔需要任何 access 授權就 clone 到。俾 Cursor 嘅做法：

**用 HTTPS URL：**
```
https://github.com/marcopinglam-rgb/nexus-v2.git
https://github.com/marcopinglam-rgb/pillownotes-nexus.git
```

**本機（如 Cursor 喺你部機跑）：**
```
C:\Users\marco\dev\nexus-v2
C:\Users\marco\dev\pillownotes-nexus
```

**喺 Cursor 開法**：`cursor` → Open Folder → 揀 `C:\Users\marco\dev\nexus-v2`（source of truth + 原型），或 `pillownotes-nexus`（app 主體）。Cursor 會自行偵測 git repo。若 Cursor 有 Git 登入，用返你自己 account 就有 write 權限；想只讀就唔使登入（public repo）。

**推薦 order**：先讀 `NEXUS_HANDOFF.md`（第一份 context）→ 再睇 `AGENTS.md`（硬規則）→ 先改 `pillownotes-nexus`（app）。

---

*以上暫定 version 1 — 有需要繼續加，例如你試完 Cursor 之後嘅 feedback。*
