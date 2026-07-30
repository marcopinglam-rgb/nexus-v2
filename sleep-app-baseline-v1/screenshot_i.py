from playwright.sync_api import sync_playwright
import os, time
BASE = r"G:\我的雲端硬碟\AI Future Leader Competition\sleep-app-baseline"
pages = [("onboarding","1-onboarding"),("dashboard","2-dashboard"),("brain-dump","3-brain-dump"),("sleep","4-sleep"),("wind-down","5-wind-down"),("settings","6-settings")]
with sync_playwright() as p:
    b=p.chromium.launch();ctx=b.new_context(viewport={"width":390,"height":844},device_scale_factor=2)
    pg=ctx.new_page()
    pg.goto(f"file:///{BASE}/baseline-version-i-warm-depth-v2.html".replace("\\","/"),wait_until="networkidle",timeout=15000)
    time.sleep(0.5)
    for pid,pname in pages:
        if pid!="onboarding":pg.evaluate(f"navigate('{pid}')");time.sleep(0.4)
        pg.screenshot(path=os.path.join(BASE,f"baseline-I-{pname}.png"),full_page=False)
        print(f"✓ {pname}")
    pg.close();b.close()
print("Done")