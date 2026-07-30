"""Take 18 screenshots: 3 versions (E,F,G) × 6 pages."""
from playwright.sync_api import sync_playwright
import os, time

BASE = r"G:\我的雲端硬碟\AI Future Leader Competition\sleep-app-baseline"

versions = [
    ("baseline-version-e-glassmorphism.html", "E"),
    ("baseline-version-f-aurora-ui.html", "F"),
    ("baseline-version-g-japandi.html", "G"),
]

pages = [
    ("onboarding", "1-onboarding"),
    ("dashboard", "2-dashboard"),
    ("brain-dump", "3-brain-dump"),
    ("sleep", "4-sleep"),
    ("wind-down", "5-wind-down"),
    ("settings", "6-settings"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2)

    for filename, ver in versions:
        url = f"file:///{BASE}/{filename}".replace("\\", "/")
        page = context.new_page()
        page.goto(url, wait_until="networkidle", timeout=15000)
        time.sleep(0.5)

        for page_id, page_name in pages:
            if page_id != "onboarding":
                page.evaluate(f"navigate('{page_id}')")
                time.sleep(0.4)

            shot = os.path.join(BASE, f"baseline-{ver}-{page_name}.png")
            page.screenshot(path=shot, full_page=False)
            print(f"✓ {shot}")

        page.close()

    browser.close()
print("\nDone — 18 screenshots.")