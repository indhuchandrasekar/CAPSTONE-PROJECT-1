import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrangeHRMEditEmployeeTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.orangehrm.com")  
        self.driver.maximize_window()

    def login(self, username, password):
        driver = self.driver
        # Enter username
        driver.find_element(By.ID, "txtUsername").send_keys(username)

        # Enter password
        driver.find_element(By.ID, "txtPassword").send_keys(password)

        # Click "Login" button
        driver.find_element(By.ID, "btnLogin").click()

        # Wait for login to process
        time.sleep(2)

    def test_edit_employee(self):
        driver = self.driver

        # Precondition: Ensure a valid ESS-User account is available
        username = "Admin"
        password = "admin123"

        # Step 1: Login to Orange HRM
        self.login(username, password)

        # Expected Result: User should be successfully logged in and redirected to the Orange HRM dashboard
        self.assertTrue("dashboard" in driver.current_url.lower())

        # Navigate to PIM module
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(2)  # Wait for the PIM module to load

        # Search for an employee
        employee_name = "John Doe"  # Replace with an actual employee name
        driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(employee_name)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(2)  # Wait for the search results to load

        # Select the employee from the search results
        driver.find_element(By.LINK_TEXT, employee_name).click()
        time.sleep(2)  # Wait for the employee details to load

        # Edit employee details
        driver.find_element(By.ID, "btnSave").click()  # Click "Edit" button
        driver.find_element(By.ID, "personal_txtEmpFirstName").clear()
        driver.find_element(By.ID, "personal_txtEmpFirstName").send_keys("Johnathan")
        driver.find_element(By.ID, "personal_txtEmpLastName").clear()
        driver.find_element(By.ID, "personal_txtEmpLastName").send_keys("Doe Jr.")
        driver.find_element(By.ID, "btnSave").click()  # Click "Save" button
        time.sleep(2)  # Wait for the save action to complete

        # Expected Result: Confirmation message displayed and employee details updated
        success_message = driver.find_element(By.CSS_SELECTOR, "div.message.success").text
        self.assertEqual(success_message, "Successfully Saved")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
