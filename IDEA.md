# idea.md — AI-led Workshop Context & Intent

## 背景 (Background)

呢個 project（Nexus / pillownotes-nexus）並唔止係一個單純嘅產品開發任務，
而係一次 AI-led workshop 嘅實踐案例：由我（human）負責定義方向、判斷同做決策，
而 Hermes Agent 負責喺 Vibe Coding 同 Loop Engineering 嘅框架下，
持續生成、驗證、迭代實際嘅 code 同 UX flow。

呢個 workshop 嘅目的唔止係「做完一個 app」，
而係探索一種新嘅協作模式：human 負責 vision、judgment、priority，
AI agent 負責大部分實作嘅重複性勞動，並喺過程中累積可重用嘅 skill 同 memory。

## 我嘅 Perspective

- 我相信未來嘅產品開發模式會由「人手寫每一行code」轉向「人定義規則、AI執行並自我優化」。
- Loop Engineering 唔係一次性生成，而係持續咁針對固定板塊（例如 User Flow、AI Layer）
  一輪一輪迭代收斂，每一輪都留低 log 同 decision trail，等下一輪有根據去改進。
- Vibe Coding 嘅價值在於快速驗證直覺同想法，但必須配合清晰嘅 project instructions
  (AGENTS.md) 同 skill 定義 (SKILL.md)，否則AI輸出會缺乏一致性同長期記憶。
- 我期望 Hermes Agent 唔止係執行工具，而係逐步「理解」呢個project嘅產品哲學，
  並喺之後每一輪迭代自主提出改善建議，而唔淨係被動執行指令。

## Purpose

1. 驗證 AI-led workflow（vibe coding + loop engineering）
   是否能夠有效提升產品迭代速度同質素。
2. 以 Nexus（brain dump / sleep tracking PWA）作為實驗場，
   持續改善核心使用者流程：日間 brain dump → 夜晚整理 → 睡前 checkpoint
