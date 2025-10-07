import time
from selenium.webdriver.common.by import By

def test_text_box(browser):
    browser.get("https://demoqa.com/text-box")
    browser.maximize_window()

    # Remove ads blocking clicks
    browser.execute_script("""
        var ads = document.querySelectorAll('iframe, #fixedban, .Advertisement, [id*="google_ads"], [id*="Ad.Plus"]');
        ads.forEach(a => a.remove());
    """)

    # Fill fields
    browser.find_element(By.ID, "userName").send_keys("Razi Sohail")
    browser.find_element(By.ID, "userEmail").send_keys("razi@example.com")
    browser.find_element(By.ID, "currentAddress").send_keys("Karachi, Pakistan")
    browser.find_element(By.ID, "permanentAddress").send_keys("Lahore, Pakistan")

    # Scroll and click submit
    submit_btn = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    submit_btn.click()

    time.sleep(1)
    assert browser.find_element(By.ID, "output").is_displayed()
