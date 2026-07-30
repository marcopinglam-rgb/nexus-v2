# Case Version 5 — Few-shot 判決案例庫（新增 HC-10 + 版面完整性規則）

- case_version: v5
- 建立日期: 2026-07-28
- 前版本: v4
- 變更摘要:
  1. 沿用 case_version_4.md 全部案例
  2. 新增 **HC-10**: 全局框架不可壓縮/侵食任何頁面主內容
  3. 新增 **F-10**: 現有版本內容被擠壓失衡 → FAIL
  4. 新增 **C-16**: Overlay 模式正確做法 → PASS

---

## 沿用案例（承接自 case_version_4.md）

全部案例索引見 case_version_4.md，此處僅列出新增。

---

## 新增案例：v5 獨有

### Rule HC-10 — 全局框架不可壓縮主內容（新增強制否決規則）
- 規則編號: **HC-10**
- 適用頁面: 全部 6 個核心頁面（Dashboard / Brain Dump / Sleep / Wind-Down / Settings）
- 規則內容:
  - 頂部欄 + 底部導覽（含 plus button）+ bottom nav 上方 fixed text bar
    構成 global layer，只佔據上下邊界
  - Global layer **不可侵食、重排、壓縮中間主要內容**
  - Fixed text bar 應採用 **overlay** 模式（position: absolute/fixed），
    而非透過 padding-bottom 將內容向上推擠
  - **任何一頁出現以下情況，即判 HC-10 FAIL**:
    1. 主內容被擠壓到屏幕一側、版面失衡
    2. 主內容區域明顯縮小（內容區高度 < 預期的 60% 可視區域）
    3. 全頁只剩 bottom nav + text bar，中間幾乎空白
    4. 內容出現不齊、不對稱、元素重疊
- 驗證方式:
  - 截圖檢查：每頁主內容區域高度是否 ≥ 60% 螢幕高度
  - 視覺檢查：內容是否被推擠/壓縮
  - CSS 檢查：text bar 是否使用 position: absolute（overlay）而非
    透過 padding/margin 改變內容佈局

### Case F-10 — 現有版本內容被擠壓失衡
- 版本: v34–v50（center-plus 系列）
- 頁面: Brain Dump / Sleep / Wind-Down / Settings（Dashboard 除外）
- 維度: HC-10（全局框架不可壓縮主內容）
- 判決: **FAIL**
- 嚴重度: 高（影響多個頁面嘅可用性）
- 證據:
  - v34–v50 的 Brain Dump / Sleep 頁面因 fixed composer bar + bottom nav +
    topbar 三層疊加，實際內容區高度僅約 55-58% 螢幕高度
  - Brain Dump 頁面的歷史記錄列表被明顯壓縮，可視區域不足
  - Sleep 頁面內容（pills + timeline）被推擠至上半部，下半部大量留白
  - 內容出現不齊情況：部分頁面元素被推到邊緣
- 原因: 早期版本為避免 fixed bar 遮蓋內容，使用 padding-bottom 將內容
  向上推擠。這個做法雖然保證內容不被遮蓋，但實際上壓縮咗可用內容空間
- 可遷移規則:
  - Fixed text bar 必須使用 **overlay 模式**（position: absolute），
    內容區保持完整高度，bar 浮動喺內容之上
  - 內容區應有足夠的 padding/margin 確保底部內容不被 bar 遮蓋，
    但唔應該因為 bar 存在而整體縮小內容區
  - HC-10 判定標準：內容區實際可用高度 < 60% 螢幕高度即判 FAIL
  - 需要逐頁檢查（唔止 Dashboard）

### Case C-16 — Overlay Text Bar 正確做法
- 版本: v51（示範版本）
- 頁面: 全局（所有頁面底部 fixed text bar）
- 維度: HC-10（全局框架不可壓縮主內容）
- 判決: **PASS**（正確 overlay 做法）
- 嚴重度: N/A
- 證據:
  - Fixed text bar 使用 `position: absolute` 定位於 bottom nav 上方
  - 各頁面內容區保持完整高度，不受 bar 影響
  - Bar 在 display mode 時以半透明背景呈現，不干擾下方內容閱讀
  - Bar 在 input mode（按 plus）時才展開為輸入區，平時以摘要模式顯示
- 原因: Overlay 模式確保主內容區域不被壓縮，同時保留 fixed bar 的
  跨頁面持續性功能。半透明背景令 bar 不遮蓋關鍵內容
- 可遷移規則:
  - 所有後續版本的 fixed text bar 必須採用 overlay 模式
  - CSS: `position: absolute; bottom: var(--nav-h);`（非 relative/static）
  - 內容區不需要為 bar 預留 padding-bottom（或僅留最小 padding 避免遮蓋）
  - Bar 背景使用半透明 + backdrop-filter: blur 而非純色不透明

---

## 案例索引總表（v5 新增部分）

| Case ID | 版本 | 頁面 | 維度 | 判決 |
|---|---|---|---|---|
| HC-10 | — | 全局 | 全局框架不可壓縮主內容 | **強制否決規則** |
| F-10 | v34–v50 | 多頁面 | 內容被擠壓失衡 | **FAIL** |
| C-16 | v51 | 全局 | Overlay text bar 正確做法 | **PASS** |

> v5 新增 1 條強制規則（HC-10）+ 2 個案例（F-10, C-16）
