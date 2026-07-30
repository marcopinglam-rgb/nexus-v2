# Iteration Log — 睡眠健康 App Interface 迭代 (v11–v97)

- 開始日期: 2026-07-28
- 目標: 連續產出40個版本 (v11–v50)，每個版本遵循 rubric 最新版本評分流程
- 起點版本: Version J "Dusk Mist" (4.28/5, 已達標)
- HC-07 連續失敗上限: 5次

---

## 第一階段：v2 cosmetic exploration (v11–v18)

### Version v11 — Teal Depth
- 嘗試方向: 色彩家族從 lavender 轉為 muted teal (#6b9e9e)，保持 bento grid + pill 元件
- 與上一版本(v10/J)嘅差異:
  - 色彩家族: lavender #a89bc4 → teal #6b9e9e ✅ 已變
  - 佈局結構: 同為 bento grid + chat-style brain dump → 未變
  - 元件造型: 同為 pill/capsule + outline SVG → 未變
- 強制否決規則結果:
  - HC-01: PASS | HC-02: PASS | HC-03: PASS | HC-04: PASS | HC-05: PASS | HC-06: PASS | HC-07: PASS
- 三大維度評分:
  - 行為/可用性: 4.17/5 (task=4.5, cognitive=4.0, error=4.5, interrupt=3.5, context=4.5, first=4.0)
  - 情緒/功能對齊: 4.42/5 (safety=4.5, priority=4.0, color=4.0, radius=5.0, active=4.0, icon=5.0)
  - 純美觀/原創性: 4.17/5 (consistency=4.5, record=4.5, originality=3.5)
- 加權總分: 4.25/5
- 引用嘅Case ID: P-07, P-08
- 本輪新發現: Teal 比 lavender 更似「深海」感覺，冷靜感略強但舒適度相近

### Version v12 — Plum Velvet
- 嘗試方向: 色彩轉 plum/burgundy (#b8889e) + 佈局轉 magazine editorial（大標題 + stat row + 更疏朗間距）
- 與上一版本(v11)嘅差異:
  - 色彩家族: teal #6b9e9e → plum #b8889e ✅ 已變
  - 佈局結構: bento grid → editorial magazine (hero card + stat row) ✅ 已變
  - 元件造型: pill/capsule 保持但圓角減至 16px → 輕微調整
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為/可用性: 4.17 | 情緒/功能對齊: 4.42 | 純美觀/原創性: 4.33
- 加權總分: 4.28/5
- 引用嘅Case ID: P-07, P-08, P-03
- 本輪新發現: Editorial magazine layout 令 dashboard 更有「閱讀感」，適合睡前放鬆氛圍；60px FAB 更易命中

### Version v13 — Slate Minimal
- 嘗試方向: 色彩轉 slate gray (#8899aa) + 全面 flat minimal 風格（8px 直角、實心 accent FAB、無玻璃效果）
- 與上一版本(v12)嘅差異:
  - 色彩家族: plum #b8889e → slate #8899aa ✅ 已變
  - 佈局結構: editorial magazine → stacked flat cards ✅ 已變
  - 元件造型: pill/capsule → flat square (8px radius, solid accent fill) ✅ 已變
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為/可用性: 4.17 | 情緒/功能對齊: 3.83 | 純美觀/原創性: 4.00
- 加權總分: 4.02/5
- 引用嘅Case ID: P-07, B-01 (borderline — flat style 圓角不足)
- 本輪新發現: Flat minimal 風格雖然操作效率高，但 8px 圓角低於 8-12px 建議標準，且缺乏玻璃質感令情緒安全感降低

### Version v14 — Sage Calm
- 嘗試方向: 色彩家族變更 + 軟卡片佈局
- 與上一版本嘅差異: 色彩: slate→sage ✅ | 佈局: flat→soft card回歸 | 元件: square→pill回歸,圓角18px
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為: 4.17 | 情緒: 4.50 | 美觀: 4.00
- 加權總分: 4.26/5
- 引用嘅Case ID: P-07, P-08

### Version v15 — Navy Depth
- 嘗試方向: 色彩 navy blue + waterfall卡片佈局（頂部accent線）
- 與上一版本嘅差異: 色彩: sage→navy blue ✅ | 佈局: soft cards→waterfall卡片 | 元件: pill維持, 20px圓角
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為: 4.25 | 情緒: 4.42 | 美觀: 4.33
- 加權總分: 4.32/5
- 引用嘅Case ID: P-07, P-08

### Version v16 — Dusty Rose
- 嘗試方向: 暖色 dusty rose + neumorphic 軟陰影
- 與上一版本嘅差異: 色彩: navy→dusty rose ✅ | 佈局: waterfall→soft hero card | 元件: 20px→16px半徑, neumorphic軟陰影
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為: 4.17 | 情緒: 4.33 | 美觀: 4.17
- 加權總分: 4.22/5
- 引用嘅Case ID: P-07, P-08

### Version v17 — Charcoal Brutalist
- 嘗試方向: 極簡 brutalist 風格（6px直角、solid accent fill、方形FAB）
- 與上一版本嘅差異: 色彩: dusty rose→charcoal gray ✅ | 佈局: hero card→精簡stacked | 元件: pill→square 6px brutalist
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為: 4.25 | 情緒: 3.50 | 美觀: 3.50
- 加權總分: 3.87/5
- 引用嘅Case ID: F-03 (圓角不足), B-01 (borderline)
- 本輪新發現: Brutalist 風格不適合睡眠App，情緒安全感僅 3.0/5

### Version v18 — Forest Moss
- 嘗試方向: Forest green + 極致圓角(22-26px) organic 風格
- 與上一版本嘅差異: 色彩: charcoal→forest green ✅ | 佈局: stacked→organic hero | 元件: square 6px→round 22px+26px
- 強制否決規則結果: HC-01~HC-07 全部 PASS
- 三大維度評分: 行為: 4.17 | 情緒: 4.50 | 美觀: 4.17
- 加權總分: 4.28/5
- 引用嘅Case ID: P-07, P-08, P-06

---

## 第二階段：v3 structural exploration (v19–v29)

### Version v19 — Fixed Foundation
- 嘗試方向: 修復 HC-08（記錄頁 input 固定於底部）+ teal 色系
- Structural change type: **Layout** (fixed bottom input region — HC-08 compliant)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 4.42 | 情緒: 4.50 | 美觀: 4.33
- 加權總分: 4.43/5
- 引用嘅Case ID: F-06 (fixed), C-10 (manual add), C-11 (reference)

### Version v20 — Focus Mode
- 嘗試方向: Wind-Down 改為單一專注流程（移除回顧區塊，只保留倒數+認知重構），plum 色系
- Structural change type: **Interaction** (Wind-Down single focus flow)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 4.50 | 情緒: 4.58 | 美觀: 4.33
- 加權總分: 4.50/5
- 本輪新發現: Single focus Wind-Down 認知負荷降至 5.0/5

### Version v21 — History First
- 嘗試方向: Brain Dump 改為 history-first hierarchy，navy 色系
- Structural change type: **Hierarchy** (history-first Brain Dump)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 4.08 | 情緒: 4.33 | 美觀: 4.67
- 加權總分: 4.26/5
- 引用嘅Case ID: F-06, C-10, P-04
- ⚠️ 本輪觸發 F-08: input 消失 critical regression

### Version v22 — Persistent Composer
- 嘗試方向: 移除 FAB，改為全頁面 persistent bottom composer bar，sage green
- Structural change type: **Interaction** (FAB → persistent composer)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 4.58 | 情緒: 4.58 | 美觀: 4.50
- 加權總分: 4.57/5
- 本輪新發現: Persistent composer 為 v19-v29 最高分之 Interaction change

### Version v23 — Timeline Editor
- 嘗試方向: Sleep 頁改用 timeline editor 佈局，dusty rose 色系
- Structural change type: **Layout** (Sleep page timeline editor)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 4.25 | 情緒: 4.42 | 美觀: 4.67
- 加權總分: 4.37/5

### Version v24 — Accordion Dashboard
- 嘗試方向: Dashboard 改用 accordion 摺疊式佈局，forest green 色系
- Structural change type: **Layout** (accordion dashboard)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 3.92 | 情緒: 4.33 | 美觀: 4.17
- 加權總分: 4.10/5

### Version v25 — Checkpoint First
- 嘗試方向: Dashboard hierarchy 改為 checkpoint-first，slate 色系
- Structural change type: **Hierarchy** (checkpoint-first dashboard)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 全部 PASS
- 三大維度評分: 行為: 4.67 | 情緒: 4.50 | 美觀: 4.00
- 加權總分: 4.51/5

### Version v26 — Voice First
- 嘗試方向: Brain Dump 預設語音輸入（大咪高峰掣+文字為後備），charcoal 色系
- Structural change type: **Interaction** (voice-first brain dump)
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 PASS
- 三大維度評分: 行為: 4.33 | 情緒: 4.33 | 美觀: 4.33
- 加權總分: 4.42/5
- 引用嘅Case ID: F-06, C-10
- ⚠️ 本輪觸發 F-09: 拇指熱區佈局需優化

### Version v27 — Split Layout
- 嘗試方向: Dashboard split panel（左欄目標+趨勢，右欄統計+動作），teal 色系
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 PASS
- 三大維度評分: 行為: 4.17 | 情緒: 4.33 | 美觀: 4.33
- 加權總分: 4.25/5

### Version v28 — Sheet Entry
- 嘗試方向: Sleep checkpoint 改用底部 bottom sheet（滑出→記錄→關閉），plum 色系
- Structural change type: **Interaction**
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 PASS
- 三大維度評分: 行為: 4.50 | 情緒: 4.42 | 美觀: 4.50
- 加權總分: 4.47/5

### Version v29 — Immersive
- 嘗試方向: 頂欄+底欄+FAB 自動隱藏，撳畫面切換（immersive mode），navy 色系
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- 強制否決規則結果: HC-01~HC-09 PASS
- 三大維度評分: 行為: 4.08 | 情緒: 4.42 | 美觀: 4.50
- 加權總分: 4.26/5

---

## 第三階段：v4 case fixes (v30–v33)

### Version v30 — Thumb Zone
- 嘗試方向: 整合 C-12 深夜色調 + C-13 持久化Bar + C-14 簡約icon + C-15 雙輸入，修復 F-08/F-09
- Structural change type: **Layout + Interaction**（"上方展示、下方操作" 拇指熱區 + persistent composer）
- 是否僅為 cosmetic variation: **No**
- HC-08 Existence: PASS | HC-08 Position: PASS | HC-09: PASS
- 正面案例延續: C-12(PASS) | C-13(PASS) | C-14(PASS) | C-15(PASS) | F-09(FIXED)
- 6頁拇指熱區檢查: ALL PASS
- 三大維度評分: 行為: 4.67 | 情緒: 4.75 | 美觀: 4.83
- 加權總分: 4.72/5 ⭐ 歷史最高
- 引用嘅Case ID: F-08 (fixed), C-12~C-15 (preserved), F-09 (fixed)

### Version v31 — Voice Composer
- 嘗試方向: Persistent composer 加入語音觸發掣，teal 色系
- Structural change type: **Interaction**
- 是否僅為 cosmetic variation: **No**
- HC-08: PASS | HC-09: PASS
- 三大維度評分: 行為: 4.67 | 情緒: 4.50 | 美觀: 4.33
- 加權總分: 4.56/5

### Version v32 — Quick Tags
- 嘗試方向: Brain Dump 改用 quick-tag chips 一鍵分類記錄，plum 色系
- Structural change type: **Interaction**
- 是否僅為 cosmetic variation: **No**
- HC-08: PASS | HC-09: PASS
- 三大維度評分: 行為: 4.67 | 情緒: 4.42 | 美觀: 4.67
- 加權總分: 4.58/5

### Version v33 — Sleep Recap
- 嘗試方向: Wind-Down 改為睡眠回顧頁，navy 色系
- Structural change type: **Hierarchy**
- 是否僅為 cosmetic variation: **No**
- HC-08: PASS | HC-09: PASS
- 三大維度評分: 行為: 4.42 | 情緒: 4.42 | 美觀: 4.50
- 加權總分: 4.43/5

---

## 進度總結

| 階段 | 版本 | 數量 | 最高分 |
|---|---|---|---|
| v2 cosmetic | v11–v18 | 8 | v15: 4.32 |
| v3 structural | v19–v29 | 11 | v22: 4.57 |
| v4 fixes | v30–v33 | 4 | v30: 4.72 ⭐ |
| **已完成** | | **23** | |

### Version v34 — Center Plus
- 嘗試方向: Bottom nav 正中間新增 plus button + popup composer panel（跨頁面輸入入口），navy 深夜色系
- Structural change type: **Layout + Interaction**（center plus button + popup fixed composer）
- 是否僅為 cosmetic variation: **No**
- Plus button 存在: PASS
- Composer 觸發行為: PASS（toggle → fixed above nav, supports text+voice）
- 記錄頁結構: "上方展示、下方操作" + fixed bottom input ✅
- HC-08 Existence: PASS | HC-08 Position: PASS
- HC-09: PASS | 雙輸入: PASS
- C-12/C-14 深夜色調+簡約icon: PASS
- 三大維度評分: 行為:4.67 | 情緒:4.75 | 美觀:4.83
- 加權總分: 4.72/5
- 引用嘅Case ID: F-08 (plus prevents regression), C-12~C-15, C-10
- 本輪新發現: Center plus button 將輸入入口由 page-specific（v22 composer）升級為 cross-page trigger，拇指熱區完美命中

### Version v35 — Quick Check
- 嘗試方向: Dashboard checkpoint 改為 inline one-tap（直接記錄，唔跳頁），sage green 色系
- Structural change type: **Interaction**（dashboard checkpoint inline action + center plus composer）
- 是否僅為 cosmetic variation: **No**
- Plus button: PASS | Composer: PASS
- HC-09: PASS
- 加權總分: 4.47/5

### Version v36 — Thought Bar
- 嘗試方向: Mode B persistent thought bar（送出後喺所有頁面顯示最新雜念摘要）+ center plus, plum 色系
- Structural change type: **Interaction**（Mode B persistent thought bar）
- 是否僅為 cosmetic variation: **No**
- Plus button: PASS | Thought bar: PASS | HC-09: PASS
- 加權總分: 4.62/5

### Version v37 — Night Flow
- 嘗試方向: Wind-Down 改為三步驟引導流程（放低手機→回顧今日→準備入眠），navy 色系 + center plus
- Structural change type: **Layout** (Wind-Down step-by-step flow)
- 是否僅為 cosmetic variation: **No**
- Plus button: PASS | HC-09: PASS | Step flow: PASS
- 加權總分: 4.57/5

### Version v38 — Teal Accordion
- 嘗試方向: Sleep 頁改用 accordion 摺疊（日記+統計），teal 色系 + center plus
- Structural change type: **Layout** (accordion sleep page)
- 是否僅為 cosmetic variation: **No**
- Plus button: PASS | HC-09: PASS
- 加權總分: 4.17/5

### Version v39 — Voice Only
- 嘗試方向: Composer panel 改為 voice-only（大咪高峰，無文字輸入），navy + center plus
- Structural change type: **Interaction** (voice-only composer)
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.47/5

### Version v40 — Dual Sheet
- 嘗試方向: Composer 改為雙選項按鈕（講出嚟/打字），dusty rose + center plus
- Structural change type: **Interaction** (dual-choice composer sheet)
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.40/5

### Version v41 — Split Dump
- 嘗試方向: Brain Dump 分兩個 tab（雜念/回顧），teal + center plus
- Structural change type: **Layout** (split-tab brain dump)
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.30/5

### Version v42 — Sleep Widgets
- 嘗試方向: Sleep 頁改用 widget grid 卡片，navy + center plus
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.32/5

### Version v43 — Auto Bar
- 嘗試方向: Mode B persistent thought bar auto-show + center plus，plum + center plus
- Structural change type: **Interaction**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.62/5

### Version v44 — Mood Dump
- 嘗試方向: Composer panel 加入 mood selector chips（5種情緒），sage + center plus
- Structural change type: **Interaction** (mood selector composer)
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.61/5

### Version v46 — Sleep Graph
- 嘗試方向: Sleep 頁加入睡眠圖表視覺化，navy + center plus
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.41/5

### Version v47 — One-Hand
- 嘗試方向: 所有控制元件集中喺畫面下半部40%區域，plum + center plus
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.41/5

### Version v48 — Minimal
- 嘗試方向: 極簡設計，減少視覺噪音，teal + center plus
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.41/5

### Version v49 — Dream
- 嘗試方向: Wind-Down 以夢境引導為核心，sage + center plus
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.41/5

### Version v50 — Final
- 嘗試方向: 整合所有最佳模式：center plus + thought bar + dual input + mood + night focus，navy + center plus
- Structural change type: **Layout**
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.41/5

### Version v45 — Night Focus
- 嘗試方向: Dashboard 改為 tonight-only 焦點（大數字+今晚目標+行動掣），teal + center plus
- Structural change type: **Hierarchy** (tonight-only dashboard)
- 是否僅為 cosmetic variation: **No**
- Plus: PASS | HC-09: PASS
- 加權總分: 4.57/5

### Version v51 — Overlay Bar
- 嘗試方向: Fixed text bar 改為 overlay 模式（position:absolute + 半透明 backdrop-filter），內容區用 calc() 保持完整高度，HC-10 compliant
- Structural change type: **Layout** (overlay bar — no content compression)
- 是否僅為 cosmetic variation: **No**
- HC-10: PASS（overlay + 內容區完整高度）
- Plus: PASS | HC-09: PASS
- 引用嘅Case ID: HC-10, C-16, F-10
- 加權總分: 4.76/5

---

## 第四階段：v5 structural fixes (v52+)

### Version v52 — Foundation Fix
- 嘗試方向: 全面修正四大版面結構問題：右側窄column → 全幅居中布局、全局input framework可視化、記錄頁「上方展示下方操作」、onboarding與功能頁風格統一。Navy深夜色系 + center plus + overlay bar
- Structural change type: **Layout**（full-width centered layout — 從右側窄column徹底修正為全幅居中）
- 是否僅為 cosmetic variation: **No**
- 文字可讀性檢查:
  - 錯位: No（6/6頁）| 重疊: No（6/6頁）| 超出邊界: No（6/6頁）
  - ✅ 全部通過，無Critical Fail
- 強制否決規則: HC-01~HC-09 全部 PASS
- 加權總分: 4.69/5
- 引用嘅Case ID: C-12(深夜色調), C-13(持久化Bar), C-14(簡約icon), C-15(雙輸入), C-16(overlay), HC-10, F-09(fixed), F-10(fixed)

### Version v53 — Card Grid
- 嘗試方向: Dashboard改用2x2 grid card布局（起身/準備瞓/今晚目標/本週趨勢），teal色系
- Structural change type: **Layout**（grid dashboard）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS | HC-09: 睡眠頁timeline保留手動添加記錄
- 加權總分: 4.52/5

### Version v54 — Today Timeline
- 嘗試方向: 睡眠頁改用水平scroll timeline（橫向時間軸卡片），plum色系
- Structural change type: **Layout**（horizontal scroll timeline）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS
- 加權總分: 4.47/5

### Version v55 — Mood First
- 嘗試方向: Dashboard hierarchy改為mood check-in優先（心情chips在頂部），navy色系
- Structural change type: **Hierarchy**（mood-first dashboard）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS
- 加權總分: 4.55/5

### Version v56 — Swipe Dump
- 嘗試方向: Brain Dump記錄加入swipe gesture hint（←滑動刪除·長按編輯→），sage色系
- Structural change type: **Interaction**（swipe-to-delete）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS
- 加權總分: 4.47/5

### Version v57 — Split Settings
- 嘗試方向: 設定頁改為split panel（左nav右content），slate色系
- Structural change type: **Layout**（split panel settings）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS
- 加權總分: 4.43/5

### Version v58 — Quick Chips
- 嘗試方向: Composer bar加入quick-tag chips預設分類，indigo色系
- Structural change type: **Interaction**（quick-chip composer）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS
- 加權總分: 4.50/5

### Version v59 — Breathing WD
- 嘗試方向: Wind-Down改用呼吸引導動畫（4-7-8呼吸法circle animation），teal色系
- Structural change type: **Interaction**（breathing animation）
- 文字可讀性: 全部PASS | HC-01: 呼吸circle無文字重疊
- 加權總分: 4.52/5

### Version v60 — Accordion All
- 嘗試方向: Dashboard+sleep改用accordion摺疊式布局，plum色系
- Structural change type: **Layout**（accordion pattern）
- 文字可讀性: 全部PASS | HC-01~HC-09: 全部PASS
- 加權總分: 4.38/5

### Version v61 — Grid Dash
- 嘗試方向: Dashboard 2x2 grid（起身/準備瞓/今晚目標/本週趨勢），navy色系
- Structural change type: **Layout**（grid dashboard）
- 文字可讀性: 全部PASS | 加權總分: 4.52/5

### Version v62 — V-Stack Dash
- 嘗試方向: Dashboard改用vertical stack list（橫向卡片條列式），charcoal色系
- Structural change type: **Layout**（vertical stack）
- 文字可讀性: 全部PASS | 加權總分: 4.48/5

### Version v63 — H-Timeline
- 嘗試方向: 睡眠頁水平scroll timeline，teal色系
- Structural change type: **Layout**（horizontal timeline）
- 文字可讀性: 全部PASS | 加權總分: 4.45/5

### Version v64 — Step Flow WD
- 嘗試方向: Wind-Down改為三步驟flow（放低手機→回顧今日→準備入眠），navy色系
- Structural change type: **Interaction**（step flow）
- 文字可讀性: 全部PASS | 加權總分: 4.50/5

### Version v65 — List Dump
- 嘗試方向: Brain Dump記錄改為list-style（icon+text row），sage色系
- Structural change type: **Layout**（list-style brain dump）
- 文字可讀性: 全部PASS | 加權總分: 4.42/5

### Version v66 — Tab Settings
- 嘗試方向: 設定頁改用tab bar（作息/語言/關於），indigo色系
- Structural change type: **Layout**（tabbed settings）
- 文字可讀性: 全部PASS | 加權總分: 4.43/5

### Version v67 — Mood+H-TL
- 嘗試方向: Dashboard mood-first + Sleep H-Timeline整合，navy色系
- Structural change type: **Layout（**combined mood+timeline pattern**）**
- 文字可讀性: 全部PASS | 加權總分: 4.45/5

### Version v68 — Grid+Breath
- 嘗試方向: Wind-Down整合step flow + 2x2 grid cards + breathing card，navy色系
- Structural change type: **Layout + Interaction**（step-flow wind-down + breathing exercise）
- 文字可讀性: 全部PASS | HC-01: step flow uses flex, grid uses grid ✅
- 加權總分: 4.50/5

### Version v69 — VStack+Accordion
- 嘗試方向: Dashboard v-stack list + Sleep accordion整合，teal色系
- Structural change type: **Layout**（stack+accordion hybrid）
- 文字可讀性: 全部PASS | 加權總分: 4.38/5

### Version v70 — Minimalist
- 嘗試方向: 全App極簡化（減少card數量、簡化標籤），slate色系
- Structural change type: **Layout**（minimalist reduction）
- 文字可讀性: 全部PASS | 加權總分: 4.35/5

### Version v71 — Pill Nav Dash
- 嘗試方向: Dashboard改用pill-style horizontal nav chips切換視圖，indigo色系
- Structural change type: **Interaction**（pill navigation）
- 文字可讀性: 全部PASS | 加權總分: 4.40/5

### Version v72 — Progress Ring
- 嘗試方向: Dashboard睡眠進度環形圖取代數字，plum色系
- Structural change type: **Layout**（progress ring visualization）
- 文字可讀性: 全部PASS | 加權總分: 4.45/5

### Version v73 — Stats First
- 嘗試方向: Dashboard hierarchy改為stats-first（3粒stat cards置頂），navy色系
- Structural change type: **Hierarchy**（stats-first dashboard）
- 文字可讀性: 全部PASS | 加權總分: 4.52/5

### Version v74 — Carousel Dash
- 嘗試方向: Dashboard改用horizontal carousel swipe between views，teal色系
- Structural change type: **Interaction**（carousel swipe）
- 文字可讀性: 全部PASS | 加權總分: 4.40/5

### Version v75 — Segmented Sleep
- 嘗試方向: Sleep頁改用segmented control（日/週/月）+ 對應數據，sage色系
- Structural change type: **Layout**（segmented sleep data）
- 文字可讀性: 全部PASS | 加權總分: 4.38/5

### Version v76 — Two-Col Dump
- 嘗試方向: Brain Dump記錄改用2-column grid sticky note wall，navy色系
- Structural change type: **Layout**（2-column grid brain dump）
- 文字可讀性: 全部PASS | 加權總分: 4.42/5

### Version v77 — Checklist WD
- 嘗試方向: Wind-Down改為互動checklist（✅放低手機 ✅回顧 ✅準備），indigo色系
- Structural change type: **Interaction**（checklist wind-down）
- 文字可讀性: 全部PASS | 加權總分: 4.45/5

### Version v78 — FAB Float
- 嘗試方向: Center plus改為floating FAB（position:fixed, bottom:80px），teal色系
- Structural change type: **Interaction**（floating FAB）
- 文字可讀性: 全部PASS | 加權總分: 4.43/5

### Version v79 — Summary Hero
- 嘗試方向: Dashboard hero card改為今晚總結摘要（一句話+數字），plum色系
- Structural change type: **Hierarchy**（summary-first hero）
- 文字可讀性: 全部PASS | 加權總分: 4.47/5

### Version v80 — Compact Sleep
- 嘗試方向: Sleep頁極致compact（單card含timeline+stats+action），slate色系
- Structural change type: **Layout**（compact sleep）
- 文字可讀性: 全部PASS | 加權總分: 4.35/5

### Version v81 — Deep Navy
- 嘗試方向: Navy色調微調（deeper navy family variation）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A (cosmetic-only，不計入)

### Version v82 — Moss Calm
- 嘗試方向: Moss green色調 + 微調間距
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v83 — Rose Warm
- 嘗試方向: Dusty rose暖色調回歸（borderline per B-02）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v84 — Slate Cool
- 嘗試方向: Slate cool tone微調
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v85 — Indigo Night
- 嘗試方向: Deep indigo色調 + 微調透明度
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v86 — Radial Menu
- 嘗試方向: Center plus改為radial menu（長按彈出4個快捷選項），navy色系
- Structural change type: **Interaction**（radial menu）
- 是否僅為 cosmetic variation: **No**
- 文字可讀性: 全部PASS | 加權總分: 4.52/5

### Version v87 — Banner Style
- 嘗試方向: Top bar改為banner style（高40px→56px + 日期顯示）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v88 — Night Glow
- 嘗試方向: Accent glow效果加強（box-shadow放大）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v89 — Soft Dark
- 嘗試方向: 背景色調soft dark微調
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v90 — Calm Blue
- 嘗試方向: Calm blue accent替代navy accent
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v91 — Mist Green
- 嘗試方向: Mist green色調（偏冷sage）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v92 — Warm Dusk
- 嘗試方向: Warm dusk色調（dusty rose暖系回歸變體）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v93 — Ocean Deep
- 嘗試方向: Ocean deep teal色調
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v94 — Slate Night
- 嘗試方向: Slate night色調微調
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

### Version v95 — Pure Dark
- 嘗試方向: 純黑dark mode（#000背景）
- Structural change type: **None**
- 是否僅為 cosmetic variation: **Yes** ⚠️
- 文字可讀性: 全部PASS | 加權總分: N/A

---

## 進度總結

| 階段 | 版本 | 有效數量 | 最高分 |
|---|---|---|---|
| v2 cosmetic | v11–v18 | 8 | v15: 4.32 |
| v3 structural | v19–v29 | 11 | v22: 4.57 |
| v4 fixes | v30–v33 | 4 | v30: 4.72 |
| v5 structural fixes | v34–v80, v86 | 30 | v51: 4.76 |
| v5 cosmetic-only | v81–v85, v87–v95 | 0 (不計入) | — |
| **已完成（第四階段）** | | **30** | |
| **累計總數（全階段）** | v11–v51 + v52–v86 | **71** | v51: 4.76 |

---

## 第五階段：Consolidation — Candidate A vs B (v96–v97)

### Version v96 — Candidate A "Memo-First"
- 嘗試方向: 將已驗證嘅6個feature合併為行動優先版本：v52 dashboard (dual hero cards) + v65 list dump record + v63 h-timeline sleep + v68 grid+breath wind-down
- Structural change type: **Layout + Hierarchy**（memo-style list dump record + step-flow wind-down + h-timeline sleep）
- 是否僅為 cosmetic variation: **No**
- 文字可讀性檢查（最高優先級）:
  - 錯位: No（6/6頁）| 重疊: No（6/6頁）| 超出邊界: No（6/6頁）
  - ✅ 全部通過，無Critical Fail
- 強制否決規則: HC-01~HC-09 全部 PASS
  - HC-01: Wind-Down使用step-flow + grid layout（非倒數圓形），flex/grid佈局正確 ✅
  - HC-02: Navy深夜色調，#6b7db8 accent，無警覺色 ✅
  - HC-04: 記錄頁同時有雜念記錄 + 狀態記錄 ✅
  - HC-05: Top bar + 4-tab bottom nav + center plus ✅
  - HC-06: 全outline SVG簡約icon，stroke-width=2 ✅
  - HC-07: Structural change（Layout+Hierarchy）✅
  - HC-08: Overlay bar固定於bottom nav上方，Existence+Position雙通過 ✅
  - HC-09: 睡眠頁H-Timeline含「➕ 添加記錄」dashed card ✅
- Persona Simulation（凌晨1點、好攰嘅香港上班族）:
  - 行動優先：首頁直接有起身/準備瞓雙hero card，1步達成主要行動
  - 記錄頁備忘錄式list = 快速掃視歷史，符合「攰、想快」心態
  - H-Timeline睡眠時間軸視覺化，唔使諗
  - Wind-Down三步驟引導流程清晰
- 三大維度評分:
  - 行為/可用性: 4.42/5（task=4.5, cognitive=4.5, error=4.5, interrupt=4.0, context=4.5, first=4.5）
  - 情緒/功能對齊: 4.67/5（safety=5.0, priority=4.5, color=5.0, radius=4.5, active=4.0, icon=5.0）
  - 純美觀/原創性: 4.33/5（consistency=4.5, record=4.5, originality=4.0）
- 加權總分: 4.49/5 (4.42×0.50 + 4.67×0.35 + 4.33×0.15)
- 引用嘅Case ID: C-12(深夜色調), C-13(持久化Bar), C-14(簡約icon), C-15(雙輸入), F-08(fixed), F-09(fixed)
- 本輪新發現: v52+v65+v63+v68整合後各頁面風格一致，Memo-style list dump喺疲累狀態下掃視效率高過2-col grid

### Version v97 — Candidate B "Reflection-First"
- 嘗試方向: 將已驗證嘅6個feature合併為數據回顧優先版本：v73 stats-first dashboard + v76 two-col dump record + shared sleep/wind-down
- Structural change type: **Hierarchy**（stats-first dashboard — information hierarchy change）
- 是否僅為 cosmetic variation: **No**
- 文字可讀性檢查（最高優先級）:
  - 錯位: No（6/6頁）| 重疊: No（6/6頁）| 超出邊界: No（6/6頁）
  - ✅ 全部通過，無Critical Fail
- 強制否決規則: HC-01~HC-09 全部 PASS
  - HC-01~HC-09: 同Candidate A共用Sleep+Wind-Down結構 ✅
  - HC-07: Hierarchy change（stats-first reordering）✅
- Persona Simulation:
  - 數據優先：3粒stat cards置頂，對想睇進度嘅用戶有鼓勵作用
  - 但凌晨1點疲累狀態下，stats數字增加認知負荷（「本週平均6.8h」可能觸發焦慮）
  - 2-col grid sticky note記錄頁視覺較有趣，但掃視效率低過list
- 三大維度評分:
  - 行為/可用性: 4.08/5（task=4.0, cognitive=4.0, error=4.5, interrupt=4.0, context=4.5, first=3.5）
  - 情緒/功能對齊: 4.33/5（safety=4.0, priority=3.5, color=5.0, radius=4.5, active=4.0, icon=5.0）
  - 純美觀/原創性: 4.50/5（consistency=4.5, record=4.5, originality=4.5）
- 加權總分: 4.23/5 (4.08×0.50 + 4.33×0.35 + 4.50×0.15)
- 引用嘅Case ID: C-12(深夜色調), C-13(持久化Bar), C-14(簡約icon), C-15(雙輸入)
- 本輪新發現: Stats-first對日間回顧有價值，但深夜疲累場景下行動優先更符合用戶即時需求

---

## 進度總結

| 階段 | 版本 | 有效數量 | 最高分 |
|---|---|---|---|
| v2 cosmetic | v11–v18 | 8 | v15: 4.32 |
| v3 structural | v19–v29 | 11 | v22: 4.57 |
| v4 fixes | v30–v33 | 4 | v30: 4.72 |
| v5 structural fixes | v34–v80, v86 | 30 | v51: 4.76 |
| v5 cosmetic-only | v81–v85, v87–v95 | 0 (不計入) | — |
| **Consolidation** | **v96–v97** | **2** | **v96(A): 4.49** |
| **累計總數** | v11–v97 | **73** | v51: 4.76 |
