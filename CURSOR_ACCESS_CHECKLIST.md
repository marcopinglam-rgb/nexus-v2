# Cursor Pro — NEXUS Access & Authorization Checklist

> 目標：Cursor Pro 接手 NEXUS app 主力開發，執行 environment 係 Marco 自己部機（Windows）。

## A. 你已經有/已確認（唔使再搞）

| # | Access | 現狀 | 驗證 |
|---|--------|------|------|
| A1 | **GitHub repo（read/write）** | `pillownotes-nexus` + `nexus-v2` 都屬 `marcopinglam-rgb`，Marco 係 owner | ✅ gh auth logged in (`marcopinglam-rgb`)，兩個 repo 都 clone 到同 push 到 |
| A2 | **GitHub CLI auth** | token scopes 有 `repo` + `workflow`，夠 push code | ✅ |
| A3 | **Vercel 部署** | 兩邊都 live（HTTP 200），static deploy | ✅ |
| A4 | **本機 git** | `gh` 已 login，keyring 認證 | ✅ |

## B. 要 Cursor 用到需要嘅嘢（按層級）

### B1. 代碼層（最關鍵）
Cursor 要喺個 project 入面推 code 去 GitHub。兩條路：
- **（推薦）Cursor 用你自己的 GitHub account 登入** → 用返你個 PAT / OAuth，直接有 write 權限。因為你部機 `gh` 已 login，Cursor 通常會食返同一套 git credential。
- 如果想 Cursor 用獨立身份 → 喺 GitHub 開一個 **fine-grained PAT**（scope：`Contents: Read & Write` 限住淨係呢兩個 repo），貼入 Cursor Git 設定。

### B2. 部署層（可選）
- 想 Cursor 自動 deploy 去 Vercel：喺 **Vercel dashboard → Settings → Git**，將兩個 repo connect 落 Vercel 做 auto-deploy（push 就去埋 live）。而家用緊嘅 `vercel.json` + `framework:null` 已經準備好 static deploy，connect 完就會work。
- 或者維持而家模式：Hermes 幫你手動 `vercel --prod` 部署，Cursor 只推 code。

### B3. 資料/無頭檔案層
- 本機要 Cursor 開到嘅 path（視乎你想 Cursor 喺邊度開發）：
  - `C:\Users\marco\...\nexus-v2`（source of truth + 原型）
  - `C:\Users\marco\...\pillownotes-nexus`（app 主體）
  - 建議 clone/放喺一個穩定位置（例如 `C:\Users\marco\dev\`），唔好放 scratch（24h 清）。

## C. 交接後工作流建議
1. **Source of Truth 唔郁**：`nexus-v2/AGENTS.md` + `rubric`/`case` 係評分框架授權來源，Cursor 改 UI 前要對照，唔可自創標準。
2. **Hermes 轉後勤**：改 app 功能 → Cursor 主力；Hermes 做 research、評分背景、Vercel 部署、後勤文件。
3. **改 UI 睇埋 iteration_log.md**：已驗證做法（overlay bar、thumb zone、center-plus）直接跟，唔好由零諗過。

## D. 未決定事項（要你確認）
- [ ] 想唔想 Vercel auto-deploy（B2）定維持手動？
- [ ] Cursor 用你自己 GitHub 身份定獨立 PAT（B1）？
- [ ] 本機 code 放邊個穩定 path（B3）？
