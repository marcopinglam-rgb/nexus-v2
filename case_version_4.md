# Case Version 4 — Few-shot 判決案例庫（新增 v3 後發現）

- case_version: v4
- 建立日期: 2026-07-28
- 前版本: v3
- 變更摘要:
  1. 沿用 case_version_3.md 全部案例
  2. 新增 **F-08**: v21記錄頁input消失（critical regression）
  3. 新增 **C-12**: v21深夜色調正面錨點
  4. 新增 **C-13**: v22雜念持久化Bar正面錨點
  5. 新增 **C-14**: v22導覽icon簡約風格正面錨點
  6. 新增 **C-15**: v26雙輸入模式正面錨點
  7. 新增 **F-09**: v26拇指熱區佈局需優化
- 基於: 全部v11-v29版本觀察

---

## 沿用案例（承接自 case_version_3.md）

| Case ID | 版本 | 頁面 | 維度 | 判決 |
|---|---|---|---|---|
| F-01 | A/B/E | Wind-Down | 文字重疊 | FAIL |
| P-01~P-05 | C/D | 各頁面 | 多維度 | PASS |
| D-01 | H/I | 全局 | 迭代多樣性 | FAIL |
| H-01/I-01 | H/I | 全局 | 色調/icon | FAIL |
| P-07~P-09 | J | 全局 | icon/色彩/記錄 | PASS |
| J-01 | J | Dashboard | dump-pill導向 | BORDERLINE |
| F-06 | v11 | Brain Dump | input未固定 | FAIL |
| P-10 | v11 | Sleep | 手動添加記錄 | PASS |
| F-07 | v13-15 | 全局 | cosmetic overfitting | FAIL |
| P-11 | v15 | Dashboard | Waterfall card | PASS |
| P-12 | v18 | 全局 | 極致圓角 | PASS |
| B-02 | v16 | 全局 | Dusty Rose邊界 | BORDERLINE |

---

## 新增案例：v4 獨有

### Case F-08 — 記錄頁 User Input Region 完全消失（Critical Regression）
- 版本: v21 (History First)
- 頁面: Brain Dump（記錄頁）
- 維度: HC-08（記錄頁輸入區固定位置）
- 判決: **FAIL**（Critical Regression — 比 F-06 更嚴重）
- 嚴重度: **Critical**（核心功能完全喪失，即時 0 分）
- 證據:
  - v21 將 Brain Dump 改為 history-first hierarchy 時，`.dump-input-bar`
    雖然在 DOM 中存在且有 `position:absolute;bottom:0`，但在實際渲染中
    未能正確顯示於頁面底部，用戶無法看到或觸及輸入區域
  - 較 v11 的 F-06（輸入區位置浮動）更嚴重：v11 至少輸入區存在且可見，
    v21 的輸入區完全消失/不可見
  - 此為結構性變更（Hierarchy change）過程中引入嘅 regression bug
- 原因: 將 Brain Dump 從「輸入優先」改為「歷史優先」時，CSS 的 absolute
  positioning 與新的 flex 佈局產生衝突，導致輸入欄被推到可視區域外或被
  其他元素遮蓋
- 可遷移規則:
  - **HC-08 檢查必須分為兩層**:
    1. **Existence check** — 確認 user input region 存在於記錄頁 DOM 中且 `display` 非 `none`
    2. **Position check** — 確認固定喺 bottom navigation bar 正上方，可視且可觸及
  - 若 existence check 失敗 → 即時判定為 critical regression，該版本直接 0 分，
    不可視為正常迭代結果，必須停低修正
  - 若 existence check 通過但 position check 失敗 → 沿用 F-06 規則（FAIL，扣分）
  - 做 Hierarchy/Layout change 時，必須先驗證核心互動元件（input bar）冇被
    意外隱藏或推出可視範圍

### Case C-12 — v21 深夜色調為正面錨點
- 版本: v21 (History First)
- 頁面: 全局
- 維度: 情緒安全感 / 色彩和諧度
- 判決: **PASS**（正面錨點，應延續）
- 嚴重度: N/A
- 證據:
  - v21 使用 navy blue 色系（背景 #0a0e18, accent #6b7db8），
    低飽和度、偏冷/偏深中性色，非常貼近深夜入睡感
  - 雖然 v21 有 F-08 的 input 消失問題，但其**色彩氛圍**本身獨立評定為優秀
  - 深藍色調在 dark mode 下提供「深海/夜空」嘅沉浸感，零刺激
- 原因: 深夜色調家族（navy blue / deep indigo / muted teal）對睡眠 App
  而言係最安全、最有效嘅色彩方向，唔應該因為做 layout exploration
  而被放棄
- 可遷移規則:
  - 後續版本做結構性改變時，**應盡量延續 v21 嘅色調家族方向**
    （低飽和度、偏冷/偏深中性色）
  - 色彩家族可以微調（navy ↔ indigo ↔ teal），但不應跳回暖色調
    （除非有明確嘅設計假說需要驗證）
  - 若必須換色，優先考慮同家族內嘅變化（例如 navy→deep indigo），
    而非跨家族跳躍

### Case C-13 — v22 雜念持久化 Bar 為正面錨點
- 版本: v22 (Persistent Composer)
- 頁面: 全局（所有頁面底部）
- 維度: 任務完成路徑長度 / 互動模式 (HC-07 Interaction)
- 判決: **PASS**（正面錨點，應延續）
- 嚴重度: N/A
- 證據:
  - v22 將用戶寫低嘅雜念轉化為一條固定 bar（`.composer-bar`），
    喺所有頁面之間持續顯示，用戶喺任何頁面都可以直接輸入
  - 此 pattern 將 Brain Dump 嘅操作路徑由「FAB→跳轉→輸入」縮短為
    「直接輸入→Enter」，任務完成步數由 3 步減至 1 步
  - 加權總分 4.57/5，為 v19-v29 最高分
- 原因: Persistent composer bar 係 FAB 模式嘅有效替代方案。
  對深夜疲累用戶而言，減少一次點擊就係減少一次 friction
- 可遷移規則:
  - Persistent composer bar 模式應喺後續版本保留延續
  - 可作為 HC-07 Interaction model change 嘅有效範例參考
  - 若後續版本移除 persistent composer 而回復 FAB 模式，需在
    iteration log 中明確解釋原因

### Case C-14 — v22 導覽 Icon 簡約風格為正面錨點
- 版本: v22 (Persistent Composer)
- 頁面: 全局（底部導覽欄）
- 維度: 圖標風格一致性 (HC-06) / 純美觀
- 判決: **PASS**（正面錨點，應延續）
- 嚴重度: N/A
- 證據:
  - v22 的 navigation bar icon 採用極簡線條風格：
    - 首頁：兩個 rx=1.5 圓角方塊
    - 記錄：單一鉛筆線條 `<path d="M12 20h9"/>`
    - 睡眠：簡化月亮 `<path d="M21 12.79..."/>`
    - 我的：圓形 `<circle cx="12" cy="7" r="4"/>`
  - 全部 outline SVG，fill=none，stroke-width=2，風格高度統一
  - 簡約風格在 dark mode 下清晰可辨，不增加視覺噪音
- 原因: 導覽 icon 應該一眼可辨但不過度搶眼。v22 的簡約線條風格
  喺功能性同美觀之間取得最佳平衡
- 可遷移規則:
  - 後續版本嘅 navigation bar icon 應避免高細節度或裝飾性強嘅風格
  - 簡約線條風格（2-3 條 path elements per icon）為推薦方向
  - 可參考 v22 嘅簡化 moon/home icon 作為基準

### Case C-15 — v26 雙輸入模式為正面錨點
- 版本: v26 (Voice First)
- 頁面: Brain Dump（記錄頁）
- 維度: 任務完成路徑長度 / 互動模式
- 判決: **PASS**（正面錨點，應保留但需優化佈局）
- 嚴重度: N/A
- 證據:
  - v26 提供文字輸入 + 語音輸入雙選項：
    - 主要入口：大語音按鈕（100px 圓形，居中）
    - 後備入口：文字 textarea（語音按鈕下方）
  - 雙輸入模式覆蓋不同使用場景：深夜想講唔想打字 → 語音；需要精確表達 → 文字
- 原因: 雙輸入模式提升 Accessibility，尤其對深夜疲累、唔想打字嘅用戶
  語音係更友善嘅選擇。但文字作為後備保留，唔會犧牲功能完整性
- 可遷移規則:
  - 雙輸入模式（語音+文字）值得喺後續版本保留延續
  - 語音按鈕應為主要視覺焦點（較大、居中），文字輸入為次要

### Case F-09 — v26 拇指熱區佈局需優化
- 版本: v26 (Voice First)
- 頁面: Brain Dump（記錄頁）
- 維度: 錯誤/誤觸風險 / 認知負荷
- 判決: **FAIL**（佈局問題，需優化）
- 嚴重度: 中
- 證據:
  - v26 的語音按鈕（100px）置於頁面中央偏上位置，文字 textarea 在下方
  - 對於單手操作（拇指熱區在畫面下半部），語音按鈕位置偏高，
    需要伸展拇指才能觸及
  - 輸入相關元件（語音掣、文字框、送出掣）分散喺頁面不同垂直位置，
    缺乏統一嘅操作區域
- 原因: 設計時以視覺平衡為優先（居中對稱），但未充分考慮單手操作嘅
  人體工學需求。深夜用戶多數單手持機，拇指自然落在畫面下半部
- 可遷移規則:
  - **記錄頁應遵循「上方展示、下方操作」原則**:
    - 展示訊息/歷史記錄 → 置頂，可滾動
    - 所有輸入相關互動元件（文字輸入框、語音按鈕、送出按鈕）→ 集中喺畫面下半部
  - 在此基礎上同時滿足 HC-08（輸入區固定喺 bottom nav 上方）
  - 下一版本需針對記錄頁重新調整垂直資訊分佈
  - 同時檢查其他 5 個核心頁面有冇類似「核心互動元件被推離拇指熱區」嘅問題

---

## 案例索引總表（v4）

| Case ID | 版本 | 頁面 | 維度 | 判決 |
|---|---|---|---|---|
| F-01~P-05 | A~D | 各頁面 | v1 沿用 | — |
| D-01 | H/I | 全局 | 迭代多樣性 | FAIL |
| H-01/I-01 | H/I | 全局 | 色調/icon | FAIL |
| P-07~P-09 | J | 全局 | icon/色彩/記錄 | PASS |
| J-01 | J | Dashboard | dump-pill導向 | BORDERLINE |
| F-06 | v11 | Brain Dump | input未固定 | FAIL |
| P-10 | v11 | Sleep | 手動添加記錄 | PASS |
| F-07 | v13-15 | 全局 | cosmetic overfitting | FAIL |
| P-11 | v15 | Dashboard | Waterfall card | PASS |
| P-12 | v18 | 全局 | 極致圓角 | PASS |
| B-02 | v16 | 全局 | Dusty Rose邊界 | BORDERLINE |
| **F-08** | v21 | Brain Dump | **input完全消失** | **CRITICAL FAIL** |
| **C-12** | v21 | 全局 | **深夜色調正面錨點** | **PASS** |
| **C-13** | v22 | 全局 | **雜念持久化Bar** | **PASS** |
| **C-14** | v22 | 導覽 | **icon簡約風格** | **PASS** |
| **C-15** | v26 | Brain Dump | **雙輸入模式** | **PASS** |
| **F-09** | v26 | Brain Dump | **拇指熱區需優化** | **FAIL** |

> v4 新增 6 個案例（F-08, C-12, C-13, C-14, C-15, F-09）