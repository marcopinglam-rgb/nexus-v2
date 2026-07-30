from playwright.sync_api import sync_playwright
import os, time
BASE = r"G:\我的雲端硬碟\AI Future Leader Competition\sleep-app-baseline"
pages = [("onboarding","1-onboarding"),("dashboard","2-dashboard"),("brain-dump","3-brain-dump"),("sleep","4-sleep"),("wind-down","5-wind-down"),("settings","6-settings")]
with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width":390,"height":844},device_scale_factor=2)
    pg = ctx.new_page()
    pg.goto(f"file:///{BASE}/baseline-version-h-warm-depth.html".replace("\\","/"), wait_until="networkidle", timeout=15000)
    time.sleep(0.5)
    for pid,pname in pages:
        if pid!="onboarding": pg.evaluate(f"navigate('{pid}')"); time.sleep(0.4)
        shot = os.path.join(BASE,f"baseline-H-{pname}.png")
        pg.screenshot(path=shot,full_page=False)
        print(f"✓ {pname}")
    pg.close(); browser.close()
print("Done")