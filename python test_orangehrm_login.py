import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrangeHRMLoginTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.orangehrm.com")
        self.driver.maximize_window()

    def test_TC_Login_01(self):
        driver = self.driver
        # Precondition: Ensure a valid ESS-User account
        username = "Admin"
        password = "admin123"

        # Step 1: Enter username
        driver.find_element(By.ID, "txtUsername").send_keys(username)

        # Step 2: Enter password
        driver.find_element(By.ID, "txtPassword").send_keys(password)

        # Step 3: Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Expected Result: The User is logged in successfully
        time.sleep(2)  # Wait for login to process
        self.assertTrue("dashboard" in driver.current_url.lower())

    def test_TC_Login_02_invalid_username(self):
        driver = self.driver
        # Step 1: Enter invalid username
        driver.find_element(By.ID, "txtUsername").send_keys("invalidUser")

        # Step 2: Enter password
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")

        # Step 3: Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Expected Result: Error message displayed
        time.sleep(2)  # Wait for login to process
        error_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(error_message, "Invalid credentials")

    def test_TC_Login_03_invalid_password(self):
        driver = self.driver
        # Step 1: Enter username
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")

        # Step 2: Enter invalid password
        driver.find_element(By.ID, "txtPassword").send_keys("invalidPass")

        # Step 3: Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Expected Result: Error message displayed
        time.sleep(2)  # Wait for login to process
        error_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(error_message, "Invalid credentials")

    def test_TC_Login_04_blank_username(self):
        driver = self.driver
        # Step 1: Leave username blank
        driver.find_element(By.ID, "txtUsername").send_keys("")

        # Step 2: Enter password
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")

        # Step 3: Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Expected Result: Error message displayed
        time.sleep(2)  # Wait for login to process
        error_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(error_message, "Username cannot be empty")

    def test_TC_Login_05_blank_password(self):
        driver = self.driver
        # Step 1: Enter username
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")

        # Step 2: Leave password blank
        driver.find_element(By.ID, "txtPassword").send_keys("")

        # Step 3: Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Expected Result: Error message displayed
        time.sleep(2)  # Wait for login to process
        error_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(error_message, "Password cannot be empty")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
