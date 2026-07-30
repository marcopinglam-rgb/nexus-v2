# Judge Prompt Version 1 — /goal 指令(睡眠健康App Interface迭代優化)

- judge_prompt_version: v1
- 建立日期: 2026-07-28
- 依賴文件: rubric_version_1.md, case_version_1.md

---

## 使用方式

在 Hermes Agent 輸入 `/goal`,接續貼上以下完整內容以啟動持久目標。

---

/goal

# 目標:睡眠健康 App Interface 迭代優化

## Outcome(完成狀態)
基於已完成嘅7個baseline版本(A/B/C/D/E/F/G)嘅評分結果,持續迭代產出新版本,
直到有一個版本喺 rubric_version_1.md 定義嘅加權總分達到 4.2/5 以上,並且
冇任何一項觸犯強制否決規則(見 rubric_version_1.md 第1節)。

## Verification(驗收方式)
每一輪產出後,必須依序執行:

1. 用 Playwright 對6個核心頁面(Onboarding/首頁/記錄頁/睡眠頁/Wind-Down頁/我的)截圖
2. 先檢查 rubric_version_1.md 第1節「強制否決規則」(HC-01至HC-05),
   任何一項不合格,該版本直接判0分,不進入加權計算,並於下一輪重做
3. 通過強制否決規則後,執行第3節「Persona Simulation」——先扮演凌晨1點
   仲瞓唔著、好攰嘅香港上班族,實際模擬走一次核心流程,再用模擬結果評分
   行為/可用性維度
4. 按 rubric_version_1.md 第2節逐維度評分(1-5分),色彩和諧度需依照
   2.2.1 嘅五步驟推理法(先描述色相/飽和度/明度,再判斷色系關係,
   再判斷飽和度區間,最後對照標準給分)
5. 讀取 case_version_1.md,若新版本情況接近某個既有 Case ID,必須在
   理由中明確引用該 Case ID 說明;若不完全匹配任何案例,需說明最接近
   邊個案例及具體差異點
6. 計算加權總分:
   總分 = (行為/可用性平均分 × 0.50) + (情緒/功能對齊平均分 × 0.35)
        + (純美觀/原創性平均分 × 0.15)

## 評分Rubric
完整評分標準請參照 rubric_version_1.md,包含:
- 第1節:強制否決規則(HC-01至HC-05)
- 第2節:三大類評分維度與定義(行為/可用性50%、情緒/功能對齊35%、
  純美觀/原創性15%)
- 第3節:Persona Simulation(深夜疲累用戶模擬)前置步驟

## Few-shot 案例參照
完整案例庫請參照 case_version_1.md,共9個已校準案例(F-01至F-03為FAIL、
P-01至P-05為PASS、B-01為BORDERLINE),涵蓋色彩和諧度、背景明度、圓角
處理、Wind-Down排版、記錄呈現模式、Active State六大判決依據。

## Constraints(不可改動)
- 全局框架:頂部欄(左Logo/標題,右設定圖示)+ 底部導覽(首頁/記錄/睡眠/
  我的四個分頁)+ 浮動快速按鈕FAB,不可增減
- 必須包含6個核心頁面內容範圍,不可刪減或合併:
  1. Onboarding(價值主張、目標睡眠時間、作息類型、通知權限)
  2. 首頁Dashboard(今日快照卡、Brain Dump常駐輸入框、Checkpoint按鈕、
     晨間回顧卡片、本週趨勢圖)
  3. 記錄頁Brain Dump(文字/語音輸入、AI自動分類標籤、歷史時間軸、
     轉存訊息入口)
  4. 睡眠頁(起身/瞓覺大按鈕、Still Awake修正、可編輯睡眠日記、
     趨勢圖+AI摘要)
  5. Wind-Down頁(10-3-2-1-0倒數、今日記錄回顧、認知重構引導)
  6. 我的/設定頁(作息模式、通知偏好、語言切換、週報統計、隱私設定)
- 唔可以用高飽和刺激色、密集資訊、急促動畫

## Iteration Policy(每輪之間要記錄)
每一輪完成後,必須記錄:
- 呢一輪參考咗邊個舊版本或Case ID嘅邊個元素
- 呢一輪嘗試改進緊邊個維度嘅分數
- judge嘅評分理由同扣分位置,下一輪要針對性修正
- 若本輪新增值得列為新Case嘅發現(新PASS/FAIL/BORDERLINE案例),
  記錄下來供後續補入 case_version_2.md

## Error Handling(卡住時匯報)
- 如果連續3輪都未能通過強制否決規則,停低並向用戶匯報具體卡住嘅原因,
  唔好自行降低標準
- 如果Playwright截圖失敗或者渲染異常,立即停低匯報,唔好跳過驗收步驟
- 如果rubric或案例庫入面有judge無法判斷嘅模糊情況,列出具體問題並
  請求用戶澄清,唔好自行假設標準

## 控制指令參考
- `/goal status` — 查看目前進度
- `/goal pause` / `/goal resume` — 暫停/恢復迭代
- `/subgoal` — 中途補充新criteria而不中斷整個loop
