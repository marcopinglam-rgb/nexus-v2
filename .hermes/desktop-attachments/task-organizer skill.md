---
name: task-organizer
description: "Use when the user pastes a message, note, or list containing one or more tasks and wants them parsed, dated, categorized, and added to a task app. Triggers: '幫我整理任務', '呢啲 task 幫我加落 Todoist/Google Tasks', '今日要做嘅事', or any raw text with multiple to-dos. ALWAYS convert raw input into a standardized task format and get user confirmation (with fine-tune) BEFORE writing to Todoist. Default write target is Todoist; Google Tasks is read-only backup unless user explicitly asks. Splits prose into tasks, infers due dates/times (今日/聽日/星期五/下星期/19:00), sorts into 🧠Daily / Socif / 📝Assignment / 🧭FYP."
metadata:
  author: user
  version: '1.1'
  language: zh-HK
---

# Task Organizer

## When to Use This Skill

Use this skill whenever the user:

- Pastes a raw message, chat log, meeting note, or brain-dump that contains one or more embedded tasks (often mixed into prose, not already a clean list), and asks you to organize / sort / add it.
- Says things like "幫我整理呢啲 task"、"加落 Todoist"、"今日/聽日要做嘅事幫我分類"。
- Wants tasks scheduled (due dates inferred) and categorized into the right list, not just dumped as one flat list.

## Core workflow (do not skip)

Every run follows this fixed order. Never write to Todoist until Step 5 is fully approved.

1. **Parse** raw input into discrete tasks
2. **Convert** each task into the standardized format below
3. **Show** the standardized draft and wait for confirm / fine-tune
4. **Apply** any user tweaks and re-show if needed
5. **Only then** send the final approved tasks to Todoist
6. **Summarize** what was added

The standardized-format preview is the product the user reviews. Todoist is only the final write destination after they are happy with the draft.

**Default write target: Todoist.** As of 2026-07-10, the user migrated all tasks from Google Tasks into matching Todoist projects and wants Todoist to be the primary place new tasks get added going forward. Google Tasks keeps its original 4 lists as a historical backup — do not write new tasks there unless the user explicitly says to use Google Tasks for a specific request.

The user has these four categories, mirrored as Todoist projects (created 2026-07-10):

| Category | Todoist project name | Typical content |
|---|---|---|
| Daily | 🧠Daily | Routine personal life-admin, chores, non-project tasks with no clear academic/social tag |
| Social | Socif | Social / social-media / community / event-related tasks |
| Assignment | 📝Assignment | Coursework, homework, class deliverables |
| FYP | 🧭FYP | Final Year Project (thesis/capstone) related tasks |

Do not assume project IDs are fixed — always resolve them fresh each run (via Todoist `find-projects`) since IDs can change if the user recreates a project. The same 4 lists still exist in Google Tasks (untouched, for backup/reference) — use `google_tasks-list-task-lists` / `google_tasks-list-tasks` only if the user asks to look up or reconcile against the Google Tasks backup.

## Standardized task format

Every extracted task MUST be converted into this format before confirmation. This is the single source of truth the user reviews and edits.

| Field | Required | Rules |
|---|---|---|
| `#` | yes | 1-based row index for easy reference when tweaking |
| `title` | yes | Short, action-first task title in the same language as the input. Keep Cantonese/Chinese natural. Preserve names, numbers, specifics (e.g. "交比 Ken", "第3章"). No date/time stuffed into the title. |
| `project` | yes | One of: 🧠Daily / Socif / 📝Assignment / 🧭FYP |
| `due` | no | Resolved absolute date (YYYY-MM-DD). If a time was mentioned, append ` HH:MM` (24h). Blank if none. |
| `due_label` | no | Original relative phrase for readability (e.g. 聽日, 星期五 19:00). Blank if none. |
| `priority` | no | Todoist priority if clearly implied (p1–p4). Default blank / p4. |
| `notes` | no | Extra context, ambiguity flags, or assumptions (e.g. "下星期 → assumed Monday") |
| `flags` | no | Short tags when relevant: `ambiguous-project`, `no-due`, `assumed-date`, `needs-split`, `needs-merge` |

### Preview table (always use this shape)

Present the draft to the user as:

```
| # | title | project | due | due_label | priority | notes / flags |
|---|---|---|---|---|---|---|
| 1 | … | 📝Assignment | 2026-07-19 | 聽日 |  |  |
| 2 | … | 🧭FYP | 2026-07-18 19:00 | 今日 7點 |  |  |
```

Do not invent extra columns. Keep empty cells blank rather than writing "N/A".

## Instructions

### Step 1 — Extract individual tasks from the raw input

The user's input is often a paragraph of prose (e.g. copy-pasted from a supervisor's message or their own stream-of-consciousness), not a clean bullet list. Parse it into discrete, actionable tasks:

- Split on explicit markers first: numbered lists (1. 2. 3.), bullets (-, •), line breaks, or connector words like "同埋"、"仲有"、"另外"、"之後"、"再"。
- If it's one continuous sentence with multiple verbs/asks, split by each distinct action (e.g. "幫我覆咗個 email 之後去交返份 report" → 2 tasks: 覆 email；交 report).
- Draft each task's `title` as a short, action-first phrase in the same language as the input (keep Cantonese/Chinese phrasing natural, don't over-translate). Preserve any names, numbers, or specifics mentioned (e.g. "交比 Ken" 、"第3章").
- Keep any explicit deadline/date phrase attached to its task for Step 3 — it becomes `due_label`, not part of `title`.

### Step 2 — Resolve the real Todoist project IDs

Before creating anything (but after building the draft is fine — IDs are only needed at write time), call Todoist `find-projects` to get the current projects and their IDs. Match by name to 🧠Daily / Socif / 📝Assignment / 🧭FYP (exact or close match — emoji may render inconsistently, so match on the text part too, e.g. "Daily", "Assignment", "FYP", "Socif").

If a project is missing, ask the user whether to create it (`add-projects`) or fall back to 🧠Daily. Do this during the confirmation loop if discovered late — never silently invent a project.

### Step 3 — Infer due date/time and fill standardized fields

Current date/time and timezone (Asia/Hong_Kong) are available in context — always resolve relative expressions against *that*, never against your training cutoff.

Resolution rules:
- "今日" → today's date.
- "聽日"/"明天" → today + 1 day.
- "後日" → today + 2 days.
- A weekday name alone (e.g. "星期五") → the next upcoming occurrence of that weekday (if today IS that weekday and no "下" prefix, treat it as today; if "下星期五"/"next Friday", jump to the following week's occurrence).
- "呢個週末" → the upcoming Saturday.
- "下星期"/"next week" with no specific day → default to the Monday of next week, and set `flags` to `assumed-date` plus a note.
- "月底"/"end of month" → the last day of the current month.
- Explicit dates (e.g. "7月15日", "15/7", "7/15") → parse directly, assuming current year unless a year is given.
- No date mentioned at all → leave `due` and `due_label` blank; set `flags` to `no-due`.

If the user mentions a specific time (e.g. "7點"/"19:00"), put it in `due` as `YYYY-MM-DD HH:MM` and keep `title` clean. Todoist's `dueString` accepts this at write time — do not prepend time into the title (that was only needed for the old Google Tasks workflow).

(Historical note: Google Tasks' API only stores the date portion of `due` and discards time — this is why the migration to Todoist happened. If the user ever asks to also add something to the Google Tasks backup, remember that limitation still applies there.)

### Step 4 — Categorize each task into a project

Use the content of the task (not just keywords) to decide `project`:
- Mentions of a class, homework, submission, professor, coursework deliverable → 📝Assignment
- Mentions of the final year project / thesis / capstone / supervisor meeting about the project → 🧭FYP
- Mentions of social media, events, community, group activities, marketing/social posts → Socif
- General personal errands, admin, health/fitness, shopping, life logistics with no other clear tag → 🧠Daily

If a task is genuinely ambiguous between two categories, pick the best default, set `flags` to `ambiguous-project`, and explain in `notes` so the user can correct it in one pass during confirmation.

### Step 5 — Convert to standardized format, confirm, then fine-tune

**Hard gate:** Do not call Todoist `add-tasks` (or any write tool) until this step is fully approved.

1. Build the full standardized preview table from Steps 1–4.
2. Show it via `confirm_action` with the complete table in the `placeholder` field.
3. Phrase the question so the user knows they can edit before anything is sent, e.g.:

> 「以下係 standardized format 草稿。想改 title / due / project、拆開或合併，直接講；確認後先會加去 Todoist。」

4. If the user replies with tweaks (wording, date, project, split, merge, priority, notes):
   - Apply the changes to the standardized draft
   - Re-show an updated preview with a fresh `confirm_action`
   - Repeat until they explicitly approve
5. Only after explicit approval, proceed to Step 6.

Never treat silence, partial feedback, or "改吓先" as approval. Only a clear confirm (e.g. approving the confirm_action, or saying 確認 / OK / 加啦 / send) unlocks the Todoist write.

### Step 6 — Create the tasks in Todoist

For each **approved** standardized row, call Todoist `add-tasks` (batch up to 25 per call) with:
- `content` ← `title`
- `projectId` ← resolved ID for `project` (from Step 2)
- `dueString` ← `due` if present (omit if blank)
- `description` ← `notes` if useful (omit flags-only noise)
- `priority` ← map p1–p4 if set
- `parentId` ← only if this row was confirmed as a sub-item of another task

Only create in Google Tasks too if the user explicitly asks for it this time (it remains the backup, not a dual-write target by default).

### Step 7 — Summarize

After creation, reply with a short grouped summary (by project) confirming what was added and its due date, e.g.:

```
📝Assignment
- 交第3章報告（2026-07-15）

🧠Daily
- 覆返 Ken 個 email（今日）
```

Flag any tasks that were skipped, still need clarification, or had no due date.

## Examples

**Input:** "幫我整理下：記住聽日交返份 assignment 嘅 draft 比教授，另外今個星期五 FYP 要交 progress report 比 supervisor，仲有今日要覆返 IG 嗰個 brand collab 嘅訊息"

**Standardized draft (shown for confirm / fine-tune — nothing written to Todoist yet):**

| # | title | project | due | due_label | priority | notes / flags |
|---|---|---|---|---|---|---|
| 1 | 交返份 assignment draft 比教授 | 📝Assignment | 2026-07-19 | 聽日 |  |  |
| 2 | 交 FYP progress report 比 supervisor | 🧭FYP | 2026-07-18 | 呢個星期五 |  |  |
| 3 | 覆返 IG brand collab 嘅訊息 | Socif | 2026-07-18 | 今日 |  |  |

User may reply e.g. 「2 改做聽日 6點，3 換去 Daily」→ update rows 2–3 → re-show table → wait for confirm again.

**Only after confirm:** create all approved rows via Todoist `add-tasks` in the resolved project IDs.
