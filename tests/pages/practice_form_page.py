import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def open_form(self):
        """Open the practice form page and remove blocking ads."""
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Wait for form to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )

        # Remove ads and fixed banners
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, #fixedban, .Advertisement, [id*="google_ads"], [id*="Ad.Plus"]');
            ads.forEach(a => a.remove());
        """)
        time.sleep(1)

    def fill_form(self, first_name, last_name, email, mobile, picture_path):
        """Fill in all required form fields and submit."""
        driver = self.driver

        # First name
        driver.find_element(By.ID, "firstName").send_keys(first_name)
        # Last name
        driver.find_element(By.ID, "lastName").send_keys(last_name)
        # Email
        driver.find_element(By.ID, "userEmail").send_keys(email)
        # Gender
        driver.find_element(By.XPATH, "//label[text()='Male']").click()
        # Mobile number
        driver.find_element(By.ID, "userNumber").send_keys(mobile)

        # Scroll to make sure next elements are visible
        driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(1)

        # Date of birth
        driver.find_element(By.ID, "dateOfBirthInput").click()
        driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()

        # Subjects
        subjects_input = driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Maths")
        subjects_input.send_keys("\n")

        # Hobbies
        driver.find_element(By.XPATH, "//label[text()='Sports']").click()

        # Upload Picture
        upload = driver.find_element(By.ID, "uploadPicture")
        upload.send_keys(os.path.abspath(picture_path))

        # Current Address
        driver.find_element(By.ID, "currentAddress").send_keys("Karachi, Pakistan")

        # Scroll and remove ads again before clicking Submit
        driver.execute_script("""
            window.scrollBy(0, 400);
            var ads = document.querySelectorAll('iframe, #fixedban, .Advertisement, [id*="google_ads"], [id*="Ad.Plus"]');
            ads.forEach(a => a.remove());
        """)
        time.sleep(1)

        # Submit form
        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", submit_btn)

    def submitted(self):
        """Check if submission modal appears successfully."""
        try:
            WebDriverWait(self.driver, 15).until(
                EC.any_of(
                    EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")),
                    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for submitting')]"))
                )
            )
            return True
        except TimeoutException:
            self.driver.save_screenshot("tests/artifacts/form_submission_failed.png")
            print("❌ Modal not detected — screenshot saved at tests/artifacts/form_submission_failed.png")
            return False

