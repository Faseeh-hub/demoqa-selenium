import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_links(browser):
    browser.get("https://demoqa.com/links")
    browser.maximize_window()

    # Remove ads blocking clicks
    browser.execute_script("""
        var ads = document.querySelectorAll('iframe, #fixedban, .Advertisement, [id*="google_ads"], [id*="Ad.Plus"]');
        ads.forEach(a => a.remove());
    """)

    # Wait for the link to be visible
    link = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "simpleLink"))
    )

    href = link.get_attribute("href")
    assert "demoqa.com" in href

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
    link.click()
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[-1])
    assert "demoqa.com" in browser.current_url
