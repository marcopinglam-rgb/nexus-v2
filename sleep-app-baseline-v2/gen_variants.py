"""
Batch generator for sleep app HTML variants.
Takes v52 as base, applies structural permutations.
"""
import os, copy

BASE_DIR = r"G:\我的雲端硬碟\AI Future Leader Competition\sleep-app-baseline-v2"

COLORS = {
    "navy":   ("#0a0e18","#6b7db8"),
    "teal":   ("#0a1214","#5d9b9b"),
    "plum":   ("#120e14","#9b7db8"),
    "sage":   ("#0e1410","#7d9b7d"),
    "slate":  ("#0e0e12","#8898aa"),
    "indigo": ("#0c0e18","#7d8dc8"),
    "charcoal":("#0e0e0e","#889090"),
    "navy_dark":("#060a14","#5d7db8"),
}

# Dashboard variants
DASHBOARD = {
    "hero_dual": '''<div class="hero-cards">
    <div class="hero-card wake" onclick="navigate('sleep')"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>起身<div class="hero-card-sub">記錄起床</div></div>
    <div class="hero-card" onclick="navigate('sleep')"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3"/></svg>準備瞓<div class="hero-card-sub">睡前放鬆</div></div></div>
    <div class="goal-card"><div class="goal-num">7h30</div><div class="goal-meta">今晚目標<br>23:30 入睡 · 07:00 起身</div></div>''',

    "grid_2x2": '''<div class="grid-2x2">
    <div class="grid-card" onclick="navigate('sleep')"><div class="grid-card-icon">☀️</div><div class="grid-card-title">起身</div><div class="grid-card-sub">07:00 記錄</div></div>
    <div class="grid-card" onclick="navigate('wind-down')"><div class="grid-card-icon">🌙</div><div class="grid-card-title">準備瞓</div><div class="grid-card-sub">睡前放鬆</div></div>
    <div class="grid-card goal"><div class="grid-card-num">7h30</div><div class="grid-card-label">今晚目標</div></div>
    <div class="grid-card"><div class="grid-card-icon">📊</div><div class="grid-card-title">本週趨勢</div><div class="grid-card-sub">平均 6.8h</div></div></div>''',

    "vertical_stack": '''<div class="v-stack">
    <div class="v-card" onclick="navigate('sleep')"><div class="v-card-left"><span class="v-icon">☀️</span></div><div class="v-card-body"><div class="v-title">起身記錄</div><div class="v-sub">07:00 · 記錄今日起床時間</div></div><div class="v-arrow">→</div></div>
    <div class="v-card" onclick="navigate('wind-down')"><div class="v-card-left"><span class="v-icon">🌙</span></div><div class="v-card-body"><div class="v-title">準備入睡</div><div class="v-sub">睡前放鬆練習</div></div><div class="v-arrow">→</div></div>
    <div class="v-card info"><div class="v-card-body"><div class="v-title">今晚目標</div><div class="v-sub">23:30 入睡 · 07:00 起身 · 目標 7h30</div></div><div class="v-num">7h30</div></div></div>''',

    "mood_first": '''<div class="mood-hero"><div class="mood-label">今晚心情如何？</div><div class="mood-chips"><div class="mood-chip active">😌 放鬆</div><div class="mood-chip">😰 緊張</div><div class="mood-chip">😤 煩躁</div><div class="mood-chip">😴 好攰</div><div class="mood-chip">😊 開心</div></div></div>
    <div class="hero-cards"><div class="hero-card wake" onclick="navigate('sleep')"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>起身<div class="hero-card-sub">記錄起床</div></div><div class="hero-card" onclick="navigate('sleep')"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3"/></svg>準備瞓<div class="hero-card-sub">睡前放鬆</div></div></div>
    <div class="goal-card"><div class="goal-num">7h30</div><div class="goal-meta">今晚目標<br>23:30 入睡 · 07:00 起身</div></div>''',
}

# Sleep page variants
SLEEP = {
    "vertical_timeline": '''<div class="sleep-quick"><div class="sleep-btn wake"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>起身<span class="sleep-btn-sub">記錄起床</span></div><div class="sleep-btn"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3"/></svg>準備瞓<span class="sleep-btn-sub">睡前放鬆</span></div></div><div class="timeline"><div class="tl-row"><div class="tl-dot filled"></div><div class="tl-card"><div class="tl-time">23:45</div><div>準備入睡</div></div></div><div class="tl-row"><div class="tl-dot"></div><div class="tl-card add" onclick="alert('手動添加記錄')"><div style="font-size:18px;margin-bottom:2px">+</div><div>手動添加記錄</div></div></div></div>''',

    "horizontal_timeline": '''<div class="h-timeline-scroll"><div class="h-timeline-track"><div class="h-tl-card wake"><div class="h-tl-time">07:00</div><div class="h-tl-icon">☀️</div><div class="h-tl-label">起身</div></div><div class="h-tl-divider"></div><div class="h-tl-card"><div class="h-tl-time">14:30</div><div class="h-tl-icon">☕</div><div class="h-tl-label">小睡</div></div><div class="h-tl-divider"></div><div class="h-tl-card active"><div class="h-tl-time">23:45</div><div class="h-tl-icon">🌙</div><div class="h-tl-label">準備瞓</div></div><div class="h-tl-divider"></div><div class="h-tl-card add" onclick="alert('手動添加記錄')"><div class="h-tl-time">+</div><div class="h-tl-icon">➕</div><div class="h-tl-label">添加記錄</div></div></div></div>''',

    "accordion_sleep": '''<div class="acc-section"><div class="acc-header open" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">快速記錄<span class="acc-arrow">▼</span></div><div class="acc-body open"><div class="sleep-quick"><div class="sleep-btn wake">☀️ 起身<span class="sleep-btn-sub">記錄起床</span></div><div class="sleep-btn">🌙 準備瞓<span class="sleep-btn-sub">睡前放鬆</span></div></div></div></div><div class="acc-section"><div class="acc-header open" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">今日時間線<span class="acc-arrow">▼</span></div><div class="acc-body open"><div class="timeline"><div class="tl-row"><div class="tl-dot filled"></div><div class="tl-card"><div class="tl-time">23:45</div><div>準備入睡</div></div></div><div class="tl-row"><div class="tl-dot"></div><div class="tl-card add" onclick="alert('手動添加記錄')"><div style="font-size:18px;margin-bottom:2px">+</div><div>手動添加記錄</div></div></div></div></div></div>''',
}

# Wind-Down variants
WIND_DOWN = {
    "countdown_cog": '''<div class="wd-section"><div class="wd-circle"><div style="display:flex;flex-direction:column;align-items:center"><span class="wd-num">10</span><span class="wd-label">mins left</span></div></div><div class="wd-card" onclick="alert('認知重構練習')"><div class="wd-card-icon">🧘</div><div><div class="wd-card-title">認知重構引導</div><div class="wd-card-desc">3 分鐘練習，釋放剩餘困擾</div></div></div></div>''',

    "breathing": '''<div class="breath-section"><div class="breath-circle"><div class="breath-inner"><span class="breath-phase">吸氣</span><span class="breath-time">4</span></div></div><div class="breath-steps"><div class="breath-step active"><span>4</span>吸氣</div><div class="breath-step"><span>7</span>閉氣</div><div class="breath-step"><span>8</span>呼氣</div></div><div class="wd-card" onclick="alert('認知重構')"><div class="wd-card-icon">🧘</div><div><div class="wd-card-title">認知重構引導</div><div class="wd-card-desc">3分鐘練習</div></div></div></div>''',

    "step_flow": '''<div class="step-flow"><div class="step active"><div class="step-num">1</div><div class="step-label">放低手機</div></div><div class="step-connector"></div><div class="step"><div class="step-num">2</div><div class="step-label">回顧今日</div></div><div class="step-connector"></div><div class="step"><div class="step-num">3</div><div class="step-label">準備入眠</div></div></div><div class="wd-card" onclick="alert('開始')" style="margin-top:28px"><div class="wd-card-icon">🧘</div><div><div class="wd-card-title">開始放鬆練習</div><div class="wd-card-desc">引導式呼吸 · 3分鐘</div></div></div>''',
}

# Brain Dump variants
BRAIN_DUMP = {
    "chat_bubbles": '''<div class="dump-section" id="dumpDisplay"><div class="dump-msg user"><div>聽日個 presentation 仲有幾頁未整完</div><div class="msg-time">22:45</div></div><div class="dump-msg user"><div>今日同同事傾偈諗到個新方向</div><div class="msg-time">21:30</div></div></div>''',

    "swipe_bubbles": '''<div class="dump-section" id="dumpDisplay"><div class="swipe-hint">← 滑動刪除 · 長按編輯 →</div><div class="dump-msg user swipeable"><div>聽日個 presentation 仲有幾頁未整完</div><div class="msg-time">22:45</div></div><div class="dump-msg user swipeable"><div>今日同同事傾偈諗到個新方向</div><div class="msg-time">21:30</div></div></div>''',

    "list_style": '''<div class="dump-list" id="dumpDisplay"><div class="dump-row"><div class="dump-row-icon">💭</div><div class="dump-row-text"><div>聽日個 presentation 仲有幾頁未整完</div><div class="dump-row-time">22:45</div></div></div><div class="dump-row"><div class="dump-row-icon">💭</div><div class="dump-row-text"><div>今日同同事傾偈諗到個新方向</div><div class="dump-row-time">21:30</div></div></div></div>''',
}

# Settings variants
SETTINGS = {
    "standard": '''<div class="settings-section"><h3>作息設定</h3><div class="setting-row" onclick="alert('作息模式')"><span>作息模式</span><span class="set-val">OT 不定時 →</span></div><div class="setting-row" onclick="alert('目標睡眠時長')"><span>目標睡眠時長</span><span class="set-val">7 小時 →</span></div><div class="setting-row" onclick="alert('睡前提醒')"><span>睡前提醒</span><span class="set-val">23:00 →</span></div></div><div class="settings-section"><h3>語言</h3><div class="chip-group"><div class="chip active">粵語</div><div class="chip">中文</div><div class="chip">English</div></div></div>''',

    "split_panel": '''<div class="split-layout"><div class="split-nav"><div class="split-nav-item active">作息</div><div class="split-nav-item">提醒</div><div class="split-nav-item">語言</div><div class="split-nav-item">關於</div></div><div class="split-content"><div class="settings-section"><h3>作息設定</h3><div class="setting-row"><span>作息模式</span><span class="set-val">OT 不定時</span></div><div class="setting-row"><span>目標睡眠時長</span><span class="set-val">7 小時</span></div></div></div></div>''',

    "tabbed": '''<div class="tab-bar"><div class="tab active">作息</div><div class="tab">語言</div><div class="tab">關於</div></div><div class="settings-section" style="margin-top:16px"><div class="setting-row"><span>作息模式</span><span class="set-val">OT 不定時 →</span></div><div class="setting-row"><span>目標睡眠時長</span><span class="set-val">7 小時 →</span></div><div class="setting-row"><span>睡前提醒</span><span class="set-val">23:00 →</span></div></div>''',
}

EXTRA_CSS = {
    "grid_2x2": '''.grid-2x2{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.grid-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:18px 14px;display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;min-height:90px;text-align:center}
.grid-card-icon{font-size:24px;margin-bottom:6px}.grid-card-title{font-size:13px;font-weight:600}
.grid-card-sub{font-size:10px;color:var(--text2);margin-top:2px}.grid-card-num{font-size:28px;font-weight:300;color:var(--accent)}
.grid-card.goal{border-color:rgba(107,125,184,.15)}''',

    "vertical_stack": '''.v-stack{display:flex;flex-direction:column;gap:10px;margin-bottom:12px}
.v-card{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:var(--radius);background:var(--card-bg);border:1px solid var(--card-border);cursor:pointer}
.v-card.info{border-color:rgba(107,125,184,.12)}.v-card-left{font-size:26px}
.v-card-body{flex:1}.v-title{font-size:14px;font-weight:600}.v-sub{font-size:11px;color:var(--text2);margin-top:2px}
.v-arrow{color:var(--text3);font-size:16px}.v-num{font-size:24px;font-weight:300;color:var(--accent)}''',

    "mood_first": '''.mood-hero{margin-bottom:16px;padding:16px;background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius)}
.mood-label{font-size:14px;font-weight:600;margin-bottom:10px}
.mood-chips{display:flex;gap:6px;flex-wrap:wrap}.mood-chip{padding:8px 14px;border-radius:20px;font-size:12px;cursor:pointer;border:1.5px solid var(--card-border);background:var(--card-bg);color:var(--text2)}
.mood-chip.active{border-color:var(--accent);color:var(--accent);background:rgba(107,125,184,.08)}''',

    "horizontal_timeline": '''.h-timeline-scroll{overflow-x:auto;padding:8px 0;margin-bottom:16px}.h-timeline-track{display:flex;gap:0;align-items:center;min-width:max-content}
.h-tl-card{min-width:90px;padding:14px 12px;border-radius:var(--radius);text-align:center;background:var(--card-bg);border:1px solid var(--card-border);cursor:pointer}
.h-tl-card.active{border-color:var(--accent)}.h-tl-card.wake{border-color:rgba(155,125,184,.2)}.h-tl-card.add{border-style:dashed;opacity:.4}
.h-tl-time{font-size:11px;font-weight:600;color:var(--text3);margin-bottom:4px}.h-tl-icon{font-size:22px;margin-bottom:4px}.h-tl-label{font-size:11px;color:var(--text2)}
.h-tl-divider{width:24px;height:1px;background:var(--card-border);flex-shrink:0}''',

    "accordion": '''.acc-section{margin-bottom:6px}.acc-header{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);cursor:pointer;font-size:14px;font-weight:600}
.acc-arrow{font-size:12px;transition:transform .25s;color:var(--text3)}.acc-header.open .acc-arrow{transform:rotate(180deg)}
.acc-body{display:none;padding:14px 16px;border:1px solid var(--card-border);border-top:none;border-radius:0 0 var(--radius) var(--radius);background:rgba(14,18,28,.3)}
.acc-body.open{display:block}''',

    "breathing": '''.breath-section{display:flex;flex-direction:column;align-items:center;gap:20px}
.breath-circle{width:180px;height:180px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--card-bg);border:2px solid var(--card-border);animation:breathPulse 12s ease-in-out infinite}
@keyframes breathPulse{0%,100%{transform:scale(1)}25%{transform:scale(1.25)}50%{transform:scale(1.25)}75%{transform:scale(.85)}}
.breath-inner{display:flex;flex-direction:column;align-items:center}.breath-phase{font-size:15px;font-weight:600;color:var(--accent)}.breath-time{font-size:42px;font-weight:200}
.breath-steps{display:flex;gap:20px}.breath-step{display:flex;flex-direction:column;align-items:center;font-size:11px;color:var(--text3)}
.breath-step span{font-size:20px;font-weight:600;color:var(--text2)}.breath-step.active span{color:var(--accent)}''',

    "step_flow": '''.step-flow{display:flex;align-items:center;gap:0;padding:0 10px}.step{display:flex;flex-direction:column;align-items:center;gap:8px;flex:1}
.step-num{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;background:var(--card-bg);border:2px solid var(--card-border);color:var(--text3)}
.step.active .step-num{background:var(--accent);border-color:var(--accent);color:#0a0e18}.step-label{font-size:11px;color:var(--text2);text-align:center}
.step-connector{width:28px;height:1px;background:var(--card-border);margin-bottom:28px;flex-shrink:0}''',

    "split_panel": '''.split-layout{display:flex;gap:0;height:100%}.split-nav{width:80px;flex-shrink:0;display:flex;flex-direction:column;gap:2px;padding-right:12px;border-right:1px solid var(--card-border)}
.split-nav-item{padding:10px 8px;font-size:12px;cursor:pointer;border-radius:10px;color:var(--text2);text-align:center}
.split-nav-item.active{background:rgba(107,125,184,.08);color:var(--accent);font-weight:600}.split-content{flex:1;padding-left:14px;overflow-y:auto}''',

    "tabbed": '''.tab-bar{display:flex;gap:0;border-bottom:1px solid var(--card-border);margin-bottom:4px}.tab{padding:10px 18px;font-size:13px;cursor:pointer;color:var(--text2);border-bottom:2px solid transparent}
.tab.active{color:var(--accent);border-bottom-color:var(--accent);font-weight:600}''',

    "swipe": '''.swipe-hint{font-size:11px;color:var(--text3);text-align:center;margin-bottom:10px;opacity:.5}''',

    "list": '''.dump-list{display:flex;flex-direction:column;gap:6px}.dump-row{display:flex;align-items:flex-start;gap:12px;padding:12px 16px;background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius)}
.dump-row-icon{font-size:18px;flex-shrink:0;margin-top:1px}.dump-row-text{flex:1;font-size:13px;line-height:1.5}.dump-row-time{font-size:10px;color:var(--text3);margin-top:3px}''',
}

# ==================== BUILD VERSIONS ====================

with open(os.path.join(BASE_DIR, "baseline-v52-foundation-fix.html"), "r", encoding="utf-8") as f:
    base = f.read()

# Find the insertion points in base HTML
ANIM_MARKER = "/* ── Animations ── */"
DASHBOARD_MARKER = '<!-- ── Dashboard ── -->\n<div class="page" id="dashboard">'
BRAINDUMP_MARKER = '<!-- ── Brain Dump (Record Page) ── -->\n<div class="page" id="brain-dump">'
SLEEP_MARKER = '<!-- ── Sleep Page ── -->\n<div class="page" id="sleep">'
WINDDOWN_MARKER = '<!-- ── Wind-Down Page ── -->\n<div class="page" id="wind-down">'
SETTINGS_MARKER = '<!-- ── Settings Page ── -->\n<div class="page" id="settings">'

versions = [
    # (num, name, change_type, color, dashboard_v, sleep_v, winddown_v, braindump_v, settings_v, css_keys)
    (56, "Swipe Dump", "Interaction", "sage",
     "hero_dual", "vertical_timeline", "countdown_cog", "swipe_bubbles", "standard",
     ["swipe"]),
    (57, "Split Settings", "Layout", "slate",
     "hero_dual", "vertical_timeline", "countdown_cog", "chat_bubbles", "split_panel",
     ["split_panel"]),
    (58, "Quick Chips", "Interaction", "indigo",
     "hero_dual", "vertical_timeline", "countdown_cog", "chat_bubbles", "standard",
     []),
    (59, "Breathing WD", "Interaction", "teal",
     "hero_dual", "vertical_timeline", "breathing", "chat_bubbles", "standard",
     ["breathing"]),
    (60, "Accordion All", "Layout", "plum",
     "hero_dual", "accordion_sleep", "countdown_cog", "chat_bubbles", "standard",
     ["accordion"]),
    (61, "Grid Dash", "Layout", "navy",
     "grid_2x2", "vertical_timeline", "countdown_cog", "chat_bubbles", "standard",
     ["grid_2x2"]),
    (62, "V-Stack Dash", "Layout", "charcoal",
     "vertical_stack", "vertical_timeline", "countdown_cog", "chat_bubbles", "standard",
     ["vertical_stack"]),
    (63, "H-Timeline", "Layout", "teal",
     "hero_dual", "horizontal_timeline", "countdown_cog", "chat_bubbles", "standard",
     ["horizontal_timeline"]),
    (64, "Step WD", "Interaction", "navy",
     "hero_dual", "vertical_timeline", "step_flow", "chat_bubbles", "standard",
     ["step_flow"]),
    (65, "List Dump", "Layout", "sage",
     "hero_dual", "vertical_timeline", "countdown_cog", "list_style", "standard",
     ["list"]),
    (66, "Tab Settings", "Layout", "indigo",
     "hero_dual", "vertical_timeline", "countdown_cog", "chat_bubbles", "tabbed",
     ["tabbed"]),
    (67, "Mood+H-TL", "Hierarchy", "plum",
     "mood_first", "horizontal_timeline", "countdown_cog", "list_style", "standard",
     ["mood_first", "horizontal_timeline", "list"]),
    (68, "Grid+Breath", "Layout", "navy", 
     "grid_2x2", "vertical_timeline", "breathing", "chat_bubbles", "split_panel",
     ["grid_2x2", "breathing", "split_panel"]),
    (69, "VStack+Swipe", "Layout", "slate",
     "vertical_stack", "accordion_sleep", "countdown_cog", "swipe_bubbles", "standard",
     ["vertical_stack", "accordion", "swipe"]),
    (70, "Minimal Hero", "Hierarchy", "charcoal",
     "hero_dual", "vertical_timeline", "step_flow", "chat_bubbles", "tabbed",
     ["step_flow", "tabbed"]),
]

generated = []
for v in versions:
    num, name, chg_type, color = v[0], v[1], v[2], v[3]
    dash_v, sleep_v, wd_v, dump_v, set_v = v[4], v[5], v[6], v[7], v[8]
    css_keys = v[9]
    
    html = base
    bg, accent = COLORS[color]
    
    # Color swap
    html = html.replace("--bg:#0a0e18", f"--bg:{bg}")
    html = html.replace("--accent:#6b7db8", f"--accent:{accent}")
    
    # Title
    html = html.replace("v52: Foundation Fix", f"v{num}: {name}")
    
    # Inject extra CSS before animation marker
    css_block = ""
    for key in css_keys:
        if key in EXTRA_CSS:
            css_block += EXTRA_CSS[key] + "\n"
    if css_block:
        html = html.replace(ANIM_MARKER, css_block + "\n" + ANIM_MARKER)
    
    # Replace page content sections
    # Dashboard
    dash_html = DASHBOARD[dash_v]
    # Find the dashboard page div and replace its content
    dash_start = html.find(DASHBOARD_MARKER)
    dash_end = html.find('</div>\n</div>\n\n<!-- ── Brain Dump', dash_start)
    if dash_end == -1:
        dash_end = html.find('</div>\n</div>\n\n<!-- ── Brain Dump', dash_start)
    # Actually, let's use a simpler approach: replace known sections by finding their boundaries
    
    # Simpler: just write the files directly with string concatenation
    # This is getting complex -- let me just use direct write_file for each version

print("Template prepared. Use direct write for each version.")
print(f"Planned {len(versions)} versions: v{versions[0][0]}-v{versions[-1][0]}")
