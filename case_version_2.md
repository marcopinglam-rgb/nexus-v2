# Case Version 2 — Few-shot 判決案例庫（更新至 Version J）

- case_version: v2
- 建立日期: 2026-07-28
- 最後更新: 2026-07-28（新增 Version J 案例 + 填補 H/I placeholder）
- 基於: Baseline 第一輪(A/B/C/D) + 第二輪(E/F/G) + 第一輪 /goal 迭代產出(H/I) + 第二輪 /goal 迭代產出(J) 共10個版本
- 變更說明: 沿用 case_version_1.md 全部9個案例(F-01至F-03、P-01至P-05、B-01),
  新增版本H、I、J嘅案例,並新增一個系統性問題案例(D-01)處理「版本間多樣性不足」

---

## 沿用案例(承接自 case_version_1.md)

| Case ID | 版本 | 維度 | 判決 |
|---|---|---|---|
| F-01 | A/B/E | 強制否決(文字重疊) | FAIL |
| P-01 | C | 色彩和諧度 | PASS(最佳) |
| B-01 | E | 色彩和諧度 | BORDERLINE |
| F-02 | B | 背景明度/情緒安全感 | FAIL |
| P-02 | D | 背景明度/情緒安全感 | PASS |
| F-03 | D | 圓角處理 | FAIL |
| P-03 | D | Wind-Down排版 | PASS(最佳) |
| P-04 | C | 記錄呈現模式 | PASS |
| P-05 | D | Active State | PASS(最佳) |

(詳細內容見 case_version_1.md,此處不重複列出)

---

## 新增案例:系統性問題

### Case D-01 — 版本間多樣性不足(Diversity Collapse)
- 版本: H、I(第一輪 /goal 迭代產出)
- 頁面: 全局
- 維度: 新增維度 — 迭代多樣性(Inter-version Diversity)
- 判決: FAIL(流程性問題,非單一版本品質問題)
- 嚴重度: 高(影響整個 /goal 迭代策略的有效性)
- 證據: H、I兩個版本喺色彩、排版、元件風格上高度相似,用戶難以辨識具體差異。
  - 版本H色彩: 深藍黑 #0c0f16 + 暖金色 accent #c4a062
  - 版本I色彩: 同樣深藍黑 #0c0f16 + 暖金色 accent #c4a062（僅背景 ambient gradient 微調）
  - 兩者佈局結構完全一致: glassmorphism stacked cards、textarea-top brain dump
  - 兩者元件造型完全一致: 18px 圓角 card、emoji 💭 FAB、dot nav indicator
  - H 與 G (Japandi) 最相似, I 與 H 幾乎完全相同
- 原因: 呢個現象同 AI 生成領域嘅「多樣性收斂」(diversity collapse)類似,
  即 judge model 一旦鎖定一個「安全」解法,後續產出會傾向圍繞該解法做
  小修小補,而唔會探索新的設計方向,尤其在冇明確要求「差異化」嘅情況下
  更容易發生
- 可遷移規則: 需喺 judge prompt 入面新增「跨版本差異度」檢查機制,要求
  judge在每輪產出後,明確比較新版本與上一輪版本喺色彩、佈局、元件造型
  三個層面嘅具體差異,若差異度過低,判定為不合格並要求下一輪嘗試明顯
  不同的設計方向

---

## Case H-01 — 版本H輔助色選用暖黃色(F-04)
- 版本: H
- 頁面: 全局（特別是 Dashboard + FAB）
- 維度: 情緒安全感 / 背景與輔助色和諧度
- 判決: FAIL（對應 Case F-04）
- 嚴重度: 高（觸發 HC-02）
- 證據: 版本H使用暖金色 accent #c4a062，雖然技術上屬 earth tone 而非純黃,
  但暖金色在深夜情境下仍帶有微弱「日間/精神」聯想，飽和度雖低但色相
  偏 warm
- 原因: 暖金色 accent 在 dark mode 下雖然對比度高、視覺清晰，但對於一個
  凌晨1點失眠用戶來說，金色/暖色調會聯想到日出、咖啡、活力，與
  「準備入睡」的情緒目標有輕微衝突
- 可遷移規則: 睡眠App的輔助色不只要避開明顯的黃/橙/紅，連暖色調的
  earth tone（如暖金、琥珀、銅色）也要謹慎評估其「喚醒聯想」風險

## Case I-01 — 版本I icon風格一致性
- 版本: I
- 頁面: 全局（底部導覽 + FAB）
- 維度: 圖標風格一致性 (HC-06)
- 判決: FAIL（對應 Case F-05）
- 嚴重度: 高（觸發 HC-06）
- 證據: 版本I底部導覽使用 outline SVG icon，但 FAB 使用 emoji 💭，
  emoji 屬 filled/colored 風格，與 outline SVG 繪製邏輯完全不同，
  造成全 App icon 風格分裂
- 原因: FAB 用 emoji 可以快速增加視覺識別度，但破壞了 icon 風格統一性
- 可遷移規則: FAB icon 必須與全 App icon 使用相同繪製邏輯（全部 outline
  或全部 filled），不可用 emoji 代替。FAB 可透過加大尺寸、加背景色、
  加 glow 效果來突出，但線條邏輯必須一致

---

## 新增案例: Version J

### Case P-07 — Version J icon風格一致性達標
- 版本: J
- 頁面: 全局（頂欄、底部導覽、FAB、各頁內聯 icon）
- 維度: 圖標風格一致性 (HC-06)
- 判決: PASS（最佳 — 首個完全根治 F-05 問題的版本）
- 嚴重度: N/A
- 證據: 全 App 所有 icon（頂欄 gear、導覽4個、FAB "+"、dashboard send arrow、
  checkpoint sun/moon、brain dump edit/mic/send、sleep clock、wind-down arrow）
  全部使用 outline SVG（fill="none" + stroke="currentColor"），FAB 使用 SVG "+"
  而非 emoji，風格完全統一
- 原因: 設計時明確以 HC-06 為檢查清單項目，確保每個 SVG 都設有 fill="none"
  或透過 CSS 覆蓋，並將 FAB icon 從 emoji 改為 SVG
- 可遷移規則: 所有內聯 SVG icon 應明確設定 fill="none" 或透過父層 CSS 統一
  設定，FAB 絕對不可使用 emoji

### Case P-08 — Version J 色彩和諧度達標(lavender accent)
- 版本: J
- 頁面: 全局
- 維度: 背景與輔助色和諧度 (HC-02, HC-03)
- 判決: PASS
- 嚴重度: N/A
- 證據: 背景 deep indigo-purple #0f0d1c (H≈255°, S≈33%, L≈8%)，
  輔助色 muted lavender #a89bc4 (H≈262°, S≈25%, L≈69%)。
  兩者屬相鄰色系(purple-blue family)，飽和度 25% < 50%，
  色彩心理學 lavender = twilight/平靜/靈性，零警覺聯想
- 原因: 刻意避開 H/I 的暖色調 accent，選用冷色調 purple family 中
  最低刺激度的 lavender，完全對齊深夜入睡情境
- 可遷移規則: 睡眠App最安全的輔助色相範圍為冷色調 purple-blue-teal
  family（避開暖色調），飽和度控制在 20-50%

### Case P-09 — Version J Chat Bubble 記錄呈現模式
- 版本: J
- 頁面: Brain Dump
- 維度: 記錄呈現模式創意度
- 判決: PASS
- 嚴重度: N/A
- 證據: Brain Dump 採用 chat bubble 對話式呈現歷史記錄，用戶輸入顯示為
  右側氣泡(mine)，AI回應顯示為左側氣泡(ai)，有別於傳統 list/timeline
  呈現方式。搭配底部固定輸入欄，模擬「同自己對話」嘅體驗。
- 原因: Chat-style 呈現令 Brain Dump 感覺更似一場對話而唔係表單填寫，
  降低心理門檻，呼應產品定位「卸下雜念」而非「記錄數據」
- 可遷移規則: 記錄類頁面可考慮對話式/便條式等非傳統 list 呈現，前提係
  不增加認知負荷

### Case J-01 — Version J Dashboard Dump-Pill 導向迂迴
- 版本: J
- 頁面: Dashboard
- 維度: 任務完成路徑長度 / 認知負荷
- 判決: BORDERLINE
- 嚴重度: 低
- 證據: Dashboard 上的 dump-pill input 允許用戶輸入文字，但點擊 send arrow
  後僅導航到 Brain Dump 頁面，已輸入的文字不會被攜帶過去，用戶需重新輸入。
  對於疲累用戶可能造成輕微 frustration。
- 原因: dump-pill 設計為「快捷入口」而非「內聯提交」，但缺乏 visual cue
  說明此行為差異
- 可遷移規則: 快捷入口如果只做導航而非內聯操作，應有明確的 visual cue
  （例如箭頭 icon + "展開" 文字），或直接改為內聯提交以減少步數

---

## 更新後案例索引總表(v2 — 含 Version J)

| Case ID | 版本 | 維度 | 判決 |
|---|---|---|---|
| F-01 | A/B/E | 強制否決(文字重疊) | FAIL |
| P-01 | C | 色彩和諧度 | PASS(最佳) |
| B-01 | E | 色彩和諧度 | BORDERLINE |
| F-02 | B | 背景明度/情緒安全感 | FAIL |
| P-02 | D | 背景明度/情緒安全感 | PASS |
| F-03 | D | 圓角處理 | FAIL |
| P-03 | D | Wind-Down排版 | PASS(最佳) |
| P-04 | C | 記錄呈現模式 | PASS |
| P-05 | D | Active State | PASS(最佳) |
| D-01 | H/I | 迭代多樣性 | FAIL(系統性) |
| H-01 | H | 輔助色暖黃→情緒安全感 | FAIL(F-04) |
| I-01 | I | icon風格不一致(FAB emoji) | FAIL(F-05) |
| P-07 | J | icon風格一致性 | PASS(最佳) |
| P-08 | J | 色彩和諧度(lavender) | PASS |
| P-09 | J | Chat Bubble記錄呈現 | PASS |
| J-01 | J | Dashboard dump-pill導向 | BORDERLINE |
