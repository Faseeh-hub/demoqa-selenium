from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


class BasePage:
    """Base class for all page objects — contains shared helpers."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- Navigation ----------
    def open(self, url):
        """Navigate to the given URL."""
        self.driver.get(url)
        self.driver.maximize_window()

    # ---------- Element actions ----------
    def find(self, locator):
        """Wait for an element to be present and return it."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def type(self, locator, text):
        """Find an element, clear it, and type text."""
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def click(self, locator):
        """Safely click an element with scroll + JS fallback."""
        el = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            el.click()
        except ElementClickInterceptedException:
            # Scroll to element and retry
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            try:
                el.click()
            except ElementClickInterceptedException:
                # Last resort: JS click
                self.driver.execute_script("arguments[0].click();", el)
        except StaleElementReferenceException:
            # If the element goes stale, re-locate and JS click
            el = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", el)
