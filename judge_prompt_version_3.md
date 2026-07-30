# Judge Prompt Version 3 — 可直接接續 /goal 或 /subgoal 使用

> 版本說明: 本版本更新自 judge_prompt_version_2.md,新增針對
> HC-08(記錄頁輸入區固定)、HC-09(睡眠頁手動添加記錄)嘅檢查步驟,
> 並大幅收緊 HC-07 迭代多樣性評判邏輯,加入 cosmetic variation
> 過濾機制,防止 overfitting。

---

## 指令範本

```
/subgoal

由下一個版本開始,採用 rubric_version_3.md、case_version_3.md
作為評分依據,取代舊版本文件。請先完整讀取呢兩份文件,再繼續執行
以下規則。

## 新規則 1: 記錄頁輸入區固定位置(對應 HC-08)
記錄頁(Brain Dump / Record page)嘅 user input region 必須固定
喺 bottom navigation bar 正上方,作為固定底部輸入區(fixed bottom
input region)。唔可以因為上方 content 多少而上下浮動,亦唔可以
被推高到中段位置。上方歷史記錄內容需要自行 scroll,輸入區保持
固定。參考 case_version_3.md 嘅 Case F-06(fail範例)同 Case
C-11(pass範例)。

## 新規則 2: 睡眠頁必須提供手動添加記錄(對應 HC-09)
Sleep page 必須明確提供「手動添加記錄 / manual add record」功能,
因為用戶可能會半夜醒來、補錄、修正睡眠紀錄。呢個唔係可選加分項,
而係必要功能。之後所有版本都要保留。參考 case_version_3.md 嘅
Case C-10。

## 新規則 3: 收緊 HC-07 對「結構改變」嘅定義
由下一輪開始,以下改動 **不算** 可辨識嘅方向性改變:
- 只改色調 / hue / saturation / brightness
- 只改 border radius
- 只改 icon size / font weight / spacing 細節
- 只改陰影、描邊粗幼、透明度

要通過迭代多樣性檢查(HC-07),每個新版本至少要包含以下其中一類
真正結構性改變:

A. Layout skeleton 改變:
- 例如由卡片堆疊改做時間軸
- 由上中下三段式改做固定底部操作區 + 可滾動內容區
- 由tabbed content改做分段sheet / accordion / split layout

B. Information hierarchy 改變:
- 例如重新排序首頁卡片主次
- 將Wind-Down由資訊頁改成單一專注流程頁
- 將記錄頁由輸入優先改為歷史回顧優先,或相反

C. Interaction model 改變:
- 例如 FAB 觸發 modal 改做 persistent composer
- Sleep page 由兩粒大按鈕改做時間軸編輯器 / sheet entry flow
- 記錄頁由單一文字輸入改做 segmented input flow(文字/語音/
  快速標籤)

## 新規則 4: 每3個版本至少1次結構性大改
由而家開始,每連續3個版本入面,至少有1個版本必須屬於「layout-level
exploration」,即明確改動 layout skeleton / information hierarchy /
interaction model 其中一項。若連續3個版本都只係色彩或圓角微調,
直接判定為 overfitting,唔好再繼續產出下一個相似版本,應主動跳去
一個明顯不同嘅 layout 家族。

## 新規則 5: 每個版本都要交代改咗咩
iteration_log 之後每版都要新增以下欄位:
- Structural change type: None / Layout / Hierarchy / Interaction
- Why this version is materially different from previous version:
  用2-3句具體解釋
- Is this only a cosmetic variation? Yes/No
如果答案係 Yes, 該版本唔計入40-version exploration quota,亦
不可呈交作為達標候選版本。

## 執行順序(每完成一個版本,依序執行)
1. 用 Playwright 對6個核心頁面截圖
2. 檢查 HC-01 至 HC-09 全部強制否決規則(注意新增HC-08、HC-09),
   逐項列出pass/fail
3. 判定 Structural change type,並填寫「是否僅為cosmetic
   variation」欄位
4. 若判定為 cosmetic-only,標註該版本不計入配額,並檢查係咪已
   連續3版cosmetic-only,若係,下一版必須強制切換 layout family
5. 執行 Persona Simulation(凌晨1點瞓唔著、好攰嘅香港上班族)
6. 按三大維度評分(行為/可用性50% + 情緒/功能對齊35% +
   純美觀/原創性15%),計算加權總分
7. 引用 case_version_3.md 相關 Case ID 作為判斷依據
8. 將以上結果寫入 iteration_log.md 對應版本嘅記錄段落

## 錯誤處理
- 連續3個版本皆為 cosmetic-only(overfitting情況): 立即停低,
  匯報現況,唔好再產出下一個相似版本,等待用戶提供新方向指引,
  或者由agent主動提出3個明顯不同嘅layout家族方向俾用戶揀
- 連續3輪未能通過強制否決規則: 停低匯報具體原因,唔好自行降低標準
- Playwright截圖失敗或渲染異常: 立即停低匯報
```

---

## 使用說明

1. 將本文件連同 `rubric_version_3.md`、`case_version_3.md` 放入
   專案資料夾,取代或並存於 version 2 文件
2. 更新 `AGENTS.md` 入面嘅版本引用,確保寫明「以檔名數字最大版本
   為準」,Hermes 會自動偵測到 version 3 為最新版本
3. 於現有 `/goal` loop 入面,直接貼上「指令範本」段落作為
   `/subgoal`,唔需要 clear 現有目標重新開始
4. 之後每一版本嘅 iteration log 都應該包含 Structural change
   type 呢個新欄位,方便你日後一次過檢視40個版本時,快速篩選邊啲
   屬於真正結構探索、邊啲屬於cosmetic variation
