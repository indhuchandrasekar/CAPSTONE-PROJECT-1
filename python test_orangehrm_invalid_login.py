import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrangeHRMInvalidLoginTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.orangehrm.com") 
        self.driver.maximize_window()

    def test_invalid_login(self):
        driver = self.driver
        # Precondition: Ensure a valid ESS-User account is available
        username = "Admin"
        invalid_password = "Invalid password"

        # Step 1: Enter username
        driver.find_element(By.ID, "txtUsername").send_keys(username)

        # Step 2: Enter invalid password
        driver.find_element(By.ID, "txtPassword").send_keys(invalid_password)

        # Step 3: Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Expected Result: Error message for invalid credentials
        time.sleep(2)  # Wait for login to process
        error_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(error_message, "Invalid credentials")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
