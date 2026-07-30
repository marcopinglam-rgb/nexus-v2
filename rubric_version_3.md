# Rubric Version 3 — 評分標準

> 版本說明: 本版本在 rubric_version_2.md 基礎上新增兩項強制功能規則
> (HC-08、HC-09),並大幅收緊 HC-07(迭代多樣性)嘅定義,明確區分
> cosmetic variation 同 structural exploration,以解決 V13-V15
> 出現嘅 overfitting 問題。

---

## 第1節: 強制否決規則(Hard Constraints)

任何一項不合格即判0分,不進入加權評分。

### HC-01 Wind-Down 頁排版正確性
倒數容器必須採用 flex 或 grid 佈局,保留固定間距,"mins left"文字
不可與倒數數字重疊或互相遮擋。

### HC-02 色彩安全
輔助色不可選用帶「警覺/活力」聯想嘅色相(黃、亮橙、亮紅)作為核心
互動元件嘅主要輔助色。不可使用高飽和刺激色、密集資訊呈現、急促動畫。

### HC-03 (保留原有定義,見rubric_version_2.md)

### HC-04 核心行為功能存在
記錄頁必須同時提供 Brain Dump(腦內雜念卸載)同 Checkpoint(狀態
記錄)兩項核心行為功能。

### HC-05 全局框架完整性
頂部欄 + 底部導覽4分頁 + FAB,不可增減。6個核心頁面內容範圍不可
刪減或合併。

### HC-06 圖標一致性
全App icon必須統一風格家族,不可在同一版本內混用outline同filled
等不同繪製邏輯。

### HC-07 迭代多樣性檢查(本版本重大修訂)

**舊定義(已棄用)**: 每一輪新版本必須喺色彩家族、佈局結構、元件
造型其中至少一個層面,做出肉眼可辨識嘅方向性改變。

**新定義**: 以下改動類型 **不算** 滿足迭代多樣性要求,即使肉眼
可辨識,亦視為 cosmetic variation:
- 只改色調 / hue / saturation / brightness
- 只改 border radius
- 只改 icon size、font weight、間距數值
- 只改陰影深淺、描邊粗幼、透明度

要通過 HC-07,新版本必須包含以下三大類別其中至少一項 **結構性
改變(structural exploration)**:

**A. Layout skeleton 改變** — 例如:
- 由卡片堆疊改做時間軸呈現
- 由上中下三段式改做固定底部操作區 + 可滾動內容區
- 由 tabbed content 改做分段 sheet / accordion / split layout

**B. Information hierarchy 改變** — 例如:
- 重新排序首頁卡片主次順序
- 將 Wind-Down 由資訊頁改成單一專注流程頁
- 記錄頁由「輸入優先」改為「歷史回顧優先」,或相反方向

**C. Interaction model 改變** — 例如:
- FAB 觸發 modal 改做 persistent composer
- 睡眠頁由兩粒大按鈕改做時間軸編輯器 / sheet entry flow
- 記錄頁由單一文字輸入改做 segmented input flow(文字/語音/
  快速標籤)

**判定規則**: 每完成一個版本,必須喺 iteration log 明確標註
Structural change type(None / Layout / Hierarchy / Interaction)。
若標註為 None,即使色彩或圓角有變化,該版本判定為 cosmetic-only,
HC-07判為FAIL,並不計入有效探索版本配額。

**探索節奏要求**: 每連續3個版本之中,至少要有1個版本屬於
layout-level exploration(即 Layout / Hierarchy / Interaction
其中一項有實質改變)。若連續3個版本皆為 cosmetic-only,判定為
overfitting,系統應主動跳出目前 layout family,探索明顯不同嘅
版面方向,不可再對同一骨架做參數微調。

### HC-08 記錄頁輸入區固定位置(新增)
記錄頁(Record / Brain Dump Page)嘅 user input region 必須固定
喺 bottom navigation bar 正上方,作為 fixed bottom input region。
不可因應上方 content 高度而動態上下浮動,亦不可被推到畫面中段
位置。上方歷史記錄內容可自行 scroll,但輸入區本身位置必須固定。
違反此規則即 HC-08 判為 FAIL。

### HC-09 睡眠頁手動添加記錄(新增)
睡眠頁(Sleep Page)必須提供「手動添加記錄」功能,容許用戶自行
新增或修正睡眠紀錄,因應用戶可能半夜醒來、需要補錄或更正資料嘅
情境。此功能屬必要項目,不可省略或隱藏於不易觸及嘅位置。違反此
規則即 HC-09 判為 FAIL。

---

## 第2節: 加權評分維度

(沿用 rubric_version_2.md 定義)
- 行為/可用性: 50%
- 情緒/功能對齊: 35%
- 純美觀/原創性: 15%

達標門檻: 加權總分 ≥ 4.2/5,且全部HC-01至HC-09通過。

---

## 第3-4節: Persona Simulation、評分計算方式

(沿用 rubric_version_2.md 原有定義,不作修改)

---

## 第5節: Iteration Log 記錄格式(更新)

每完成一個版本,必須記錄以下欄位:

```
### v[XX] — [代號名稱]
- 嘗試方向: ...
- 與上一版本嘅差異: 色彩家族/佈局結構/元件造型三項各自有咩唔同
- Structural change type: None / Layout / Hierarchy / Interaction
- 是否僅為 cosmetic variation: Yes / No
- 強制否決規則結果: HC-01至HC-09逐項pass/fail
- 三大維度評分: 行為/可用性、情緒/功能對齊、純美觀/原創性
- 加權總分: X.XX/5
- 引用嘅Case ID: (參照case_version_3.md)
- 本輪新發現(如有): 值得記錄做新Case嘅觀察
```

若「是否僅為 cosmetic variation」答案為 Yes,該版本不計入有效
探索版本配額,亦不可作為達標候選版本呈交人手覆核。
