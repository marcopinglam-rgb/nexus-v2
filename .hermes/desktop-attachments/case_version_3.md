# Case Version 3 — Few-shot 判決案例庫

> 版本說明: 本版本在 case_version_2.md 基礎上新增 V11-V15 觀察所得嘅
> 新案例,重點針對「記錄頁輸入區固定位置」、「睡眠頁手動添加記錄」
> 兩項功能規則,以及「結構性 overfitting」問題嘅具體判例。
> 已完成版本 A-J 沿用字母命名,V11 起採用純數字命名。

---

## Case ID: C-10
版本: V11
頁面: 睡眠頁 (Sleep Page)
維度: 核心功能完整性
判決: PASS
嚴重度: 高(屬必要功能,非加分項)
證據: V11 睡眠頁提供「手動添加記錄」選項,容許用戶自行新增/修正
睡眠紀錄
原因: 用戶可能半夜醒來、事後補錄,或者對自動偵測結果有修正需要。
呢個唔係錦上添花嘅功能,而係核心可用性需求,缺少會直接影響
App嘅實用性
可遷移規則: 睡眠頁必須恆常保留手動添加/編輯記錄嘅入口,所有版本
不可移除或隱藏得過深,建議放置喺頁面容易觸及嘅位置(例如FAB
或頁面頂部操作區)

---

## Case ID: F-06
版本: V11
頁面: 記錄頁 (Record / Brain Dump Page)
維度: 版面結構穩定性
判決: FAIL
嚴重度: 中
證據: V11 記錄頁嘅 user input 區域位置會因應上方 content 高度而
向下浮動,冇固定喺畫面底部
原因: 輸入區位置不穩定會令用戶難以形成肌肉記憶,每次要重新搜尋
輸入框位置,對深夜疲累、認知資源有限嘅用戶尤其造成負擔
可遷移規則: 記錄頁嘅 user input region 必須固定喺 bottom
navigation bar 正上方,作為 fixed bottom input region。上方歷史
內容可自行 scroll,但輸入區本身唔可以隨 content 動態上下移動

---

## Case ID: F-07
版本: V13, V14, V15
頁面: 全部6個核心頁面
維度: 迭代多樣性(HC-07)/ 結構性探索
判決: FAIL(overfitting)
嚴重度: 高
證據: V13至V15三個連續版本之間,主要差異僅為色調(color tone)
轉換同 border radius 微調,layout skeleton、information
hierarchy、interaction model 均未見實質改變
原因: 純美觀參數嘅微調(色彩、圓角、陰影、間距)容易被誤判為
「新版本」,但實際上冇提供任何新嘅設計假說俾用戶比較,屬於
探索停滯,浪費迭代資源
可遷移規則: 迭代多樣性檢查唔可以只睇色彩/圓角呢類 cosmetic
variation,必須明確要求 layout skeleton、information hierarchy、
interaction model 其中至少一項有實質改變,方可計入有效探索版本數

---

## Case ID: C-11
版本: V12
頁面: 記錄頁
維度: 版面結構穩定性
判決: PASS(對照案例)
嚴重度: 中
證據: V12 記錄頁輸入區固定喺 bottom navigation bar 上方,不受
上方 content 長度影響
原因: 符合固定底部輸入區規則,提供穩定、可預期嘅操作位置
可遷移規則: 同 F-06,此案例作為「正確做法」嘅對照範例保留

---

## 版本命名規則備註
- 版本 A-J: 沿用字母命名,對應 case_version_2.md 既有記錄,不作
  回溯更名
- 版本 v11 起: 採用純數字命名(v11, v12, v13...v50),每版本可附加
  描述性代號(例如 v11 "Warm Ochre")作輔助識別,正式編號一律用
  v+數字
