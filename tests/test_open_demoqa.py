# tests/test_open_demoqa.py
import time

def test_open_demoqa(browser):
    browser.get("https://demoqa.com")
    time.sleep(5)  # wait for page to fully load
    title = browser.title
    print(f"Page title is: {title!r}")
    assert "DEMOQA" in title or "ToolsQA" in title, f"Unexpected title: {title}"
