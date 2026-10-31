# NEXUS — Developer Handoff & Context（俾 Cursor Pro 接手用）

> 建立：2026-10-31 | 角色分工：Cursor Pro = 主力開發 Nexus app；Hermes (Marco) = 後勤 / 輔助
> 呢份檔案 consolidate 咗兩個 repo 嘅完整 context，Cursor 可以直接讀佢上手中。

---

## 0. 一句講明

**NEXUS = 睡眠健康 PWA**。解決嘅唔係「追蹤睡眠數據」，而係**失眠成因**：腦內雜念卸載（Brain Dump）+ 認知重構（正向重構 / Reframe）。係「AI Future Leader 職涯計劃」比賽項目。核心差異化：深夜疲累用戶、單手操作、行動優先。

---

## 1. Repository 架構（兩個 repo，角色唔同）

| Repo | URL | 角色 | Live URL |
|------|-----|------|----------|
| **pillownotes-nexus** | github.com/marcopinglam-rgb/pillownotes-nexus | **實際可運行 mobile-first PWA app**（Brain Dump + Canvas + AI Copilot） | `pillownotes-nexus.vercel.app` |
| **nexus-v2** | github.com/marcopinglam-rgb/nexus-v2 | **比賽資料 + UI 原型迭代庫**（case study + 評分 docs + 大量 baseline HTML） | `nexus-v2.vercel.app` |

- `pillownotes-nexus` = **當前 prototype 主體**（改 app 功能朝呢度改）
- `nexus-v2/sleep-app-baseline-v3/` = 另一條線（AI sleep-companion demo，有 transformer.js 零樣本情緒分類 + 正向重構）。`sleep-companion-demo01.html` 100KB 完整互動 demo。

---

## 2. 產品定位（Product Philosophy）

- **痛點**：睡前腦內雜念（「未瞓，腦到轉不停」）→ 失眠
- **解法**：日間/睡前 **Brain Dump 卸載** → **認知重構（Reframe）** → **Checkpoint 睡眠追蹤**，而唔係白噪音/冥想/純數據追蹤
- **目標用戶 persona**：凌晨1點瞓唔著、好攰嘅香港上班族（OT文化、單手、想快）
- **本地化方向**：香港/亞洲 —— 彈性 OT 倒數、煩惱來源標籤、粵語 UI（roadmap 內多項項目標明香港/亞洲本地化）

---

## 3. Source of Truth（nexus-v2 repo 內，唔可以自己發明標準）

呢個 project 同一般開發唔同 —— **UI 迭代有完整評分框架**，擺系 `nexus-v2/` 根目錄：

| 文件 | 作用 |
|------|------|
| `AGENTS.md` | **專案規則總綱**。評分流程、硬性規則、案例庫維護規則、溝通語言 |
| `rubric_version_*.md` | 評分標準（強制否決規則 HC-01~HC-10、維度權重、Persona Simulation、多樣性檢查） |
| `case_version_*.md`（最新 v5） | few-shot 判決案例庫（PASS/FAIL/BORDERLINE + 可遷移規則） |
| `judge_prompt_version_*.md` | 完整 judge 指令範本（接 `/goal`） |
| `iteration_log.md` | 逐版本評分 log（v11–v97，73 個版本） |
| `IDEA.md` | workshop 哲學背景（human definies vision，AI 執行） |
| `sleep_app_feature_roadmap.csv` | 功能優先度（MoSCoW + 開發難度 + 香港本地化標記） |

**硬性規則（改 UI 前必讀 AGENTS.md，唔可用假設）**：
- 全局框架：頂部欄 + 底部導覽 4 分頁 + FAB（v34 起 center-plus），唔可增減
- 6 個核心頁面唔可以刪減/合併
- 唔可以用高飽和刺激色、密集資訊、急促動畫
- 輔助色唔用黃/亮橙/亮紅（警覺聯想）
- 全 App icon 統一風格家族（唔混 outline + filled）
- **HC-10（v5 新增）**：頂欄+底欄+fixed bar 構成 global layer，**唔可以壓縮/侵食主內容**——text bar 必須用 **overlay 模式（position:absolute）**，內容區 ≥60% 可視高度

---

## 4. 迭代成果 — 已驗證嘅最佳做法（揀 feature 直接跟）

`iteration_log.md` 有完整 73 版迭代。**最高分版本**同**可遷移做法**：

| 做法 | 版本 | 分值 | 點解 |
|------|------|------|------|
| **Overlay text bar（position:absolute + 半透明 blur）** | v51 | **4.76** ⭐ | 唔壓縮內容區（HC-10 模板） |
| **Thumb zone + persistent composer + center plus** | v30 | 4.72 | 拇指熱區 + 固定輸入列 |
| **Center-plus bottom nav（跨頁面輸入入口）** | v34 | 4.72 | FAB 位置係拇指熱區，防 input 消失 regression |
| **Persistent composer（FAB → fixed bottom bar）** | v22 | 4.57 | 認知負荷最低 |
| Foundation fix（全幅居中 + 統一 onboarding） | v52 | 4.69 | 修右側窄 column |
| **Navy 深夜色調 + outline SVG 簡約 icon** | 貫穿 | — | 情緒安全高分（safety 5.0） |

**Consolidation 決定（v96/v97）**：Candidate A「Memo-First」4.49 勝出 B「Reflection-First」4.23。理由：**深夜疲累下「行動優先」>「數據回顧」**。A 組合 = v52 dashboard（雙 hero cards）+ v65 list dump record + v63 h-timeline sleep + v68 grid+breath wind-down。

---

## 5. 而家個 App 係咩樣（pillownotes-nexus）

- **純 HTML/CSS/JS 單一 PWA**，無 build step，無 framework 依賴（只用 CDN `marked.min.js`）
- 檔案：`index.html`(454行) / `app.js`(1212行) / `styles.css`(365行) / `sw.js`(service worker) / `manifest.webmanifest`
- **兩個 app mode**：`Braindump`（🛏 預設主介面）+ `Canvas`（◈ 白色畫布，節點式）
- **架構**：`i18n` 字典（en/…)、本地數據結構 `nexusOS`、AI Copilot（Nexus Copilot：organize/brainstorm/summarize/plan/sleep）
- 底部 5 Tab（README 內文）：Dump / 睡眠 / 放鬆 / 畫布 / 更多
- **Data**：LocalStorage key `nexusOS`；mobile tab 記憶 `nexusMobileTab`
- **測試**：`python -m http.server 8899` 同一 Wi-Fi 手機測；加主畫面做 PWA standalone

---

## 6. Vercel 部署

- 兩邊都 deploy 喺 Vercel（`framework: null`，static，`outputDirectory: "."`）
- `pillownotes-nexus/vercel.json` 有完整 security headers（SW + manifest + nosniff）
- Live 驗證：`pillownotes-nexus.vercel.app` 同 `nexus-v2.vercel.app` 都 HTTP 200

---

## 7. 溝通語言

- 同 Marco 溝通用**廣東話（口語書面化）**，技術術語保留英文
- AGENTS.md 明文字：technical docs / commit 可中文可英文，通訊一律廣東話

---

## 8. 邊度搵完整資料（重要）

所有評分/案例/roadmap 嘅授權來源都喺 **nexus-v2 repo 根目錄**，唔喺 pillownotes-nexus。改 pillownotes-nexus 之前，若涉及 UX/UI 決策，先對照 `nexus-v2/AGENTS.md` + 最新 `rubric/case` 版本號（三份文件版本要一致，唔一致要向 Marco 確認）。
