import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_buttons_page(browser):
    browser.get("https://demoqa.com/buttons")
    browser.maximize_window()

    # Remove ads
    browser.execute_script("""
        var ads = document.querySelectorAll('iframe, #fixedban, .Advertisement, [id*="google_ads"], [id*="Ad.Plus"]');
        ads.forEach(a => a.remove());
    """)

    actions = ActionChains(browser)

    # Double click
    double_btn = browser.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_btn).perform()
    msg1 = browser.find_element(By.ID, "doubleClickMessage").is_displayed()

    # Right click
    right_btn = browser.find_element(By.ID, "rightClickBtn")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", right_btn)
    actions.context_click(right_btn).perform()
    time.sleep(1)
    msg2 = browser.find_element(By.ID, "rightClickMessage").is_displayed()

    # Single click
    click_btn = browser.find_element(By.XPATH, "//button[text()='Click Me']")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_btn)
    click_btn.click()
    msg3 = browser.find_element(By.ID, "dynamicClickMessage").is_displayed()

    assert msg1 and msg2 and msg3
