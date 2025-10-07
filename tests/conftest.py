import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # Set up Chrome options
    chrome_options = Options()

    # ❌ DO NOT use headless — we want to see the browser
    # chrome_options.add_argument("--headless")  # (remove or comment out)

    # ✅ Optional quality-of-life options
    chrome_options.add_argument("--start-maximized")     # open full screen
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ✅ Create Chrome WebDriver instance
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Return to tests
    yield driver

    # ✅ Close browser after test
    driver.quit()
