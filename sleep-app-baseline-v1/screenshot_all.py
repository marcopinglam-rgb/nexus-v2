"""Take 24 screenshots: 4 versions × 6 pages."""
from playwright.sync_api import sync_playwright
import os, time

BASE = r"G:\我的雲端硬碟\AI Future Leader Competition\sleep-app-baseline"
OUT = BASE

versions = [
    ("baseline-version-a-minimalist-dark.html", "A"),
    ("baseline-version-b-soft-neumorphism.html", "B"),
    ("baseline-version-c-nature-organic.html", "C"),
    ("baseline-version-d-editorial-calm.html", "D"),
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
    context = browser.new_context(
        viewport={"width": 390, "height": 844},
        device_scale_factor=2,
    )

    for filename, ver in versions:
        url = f"file:///{BASE}/{filename}".replace("\\", "/")
        page = context.new_page()
        page.goto(url, wait_until="networkidle", timeout=15000)
        time.sleep(0.5)

        for page_id, page_name in pages:
            if page_id == "onboarding":
                # Onboarding is already showing as first page
                pass
            else:
                # Navigate to the page
                page.evaluate(f"navigate('{page_id}')")
                time.sleep(0.4)

            shot_path = os.path.join(OUT, f"baseline-{ver}-{page_name}.png")
            page.screenshot(path=shot_path, full_page=False)
            print(f"✓ {shot_path}")

        page.close()

    browser.close()

print("\nDone — 24 screenshots saved.")