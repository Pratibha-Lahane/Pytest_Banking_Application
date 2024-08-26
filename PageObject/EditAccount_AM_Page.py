from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class EditAccount_AM_Page:
    Click_ViewAllAccount_Xpath = (By.XPATH, "")
    Text_Balance_Xpath = (By.XPATH, "//input[@id= 'balance']")
    Click_UpdateAccount_Xpath = (By.XPATH, "//button[@type='submit']")
    AccountUpdate_Success_Xpath = (By.XPATH, "//div[@class='success-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clicking_On_ViewAllAccount(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_ViewAllAccount_Xpath))
        element = self.driver.find_element(*EditAccount_AM_Page.Click_ViewAllAccount_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def EnteringUpdated_Balance(self, balance):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Balance_Xpath))
        element = self.driver.find_element(*EditAccount_AM_Page.Text_Balance_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(balance)

    def Click_On_UpdateAccount(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_UpdateAccount_Xpath))
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*EditAccount_AM_Page.Click_UpdateAccount_Xpath).click()

    def Validate_AccountUpdated_Status(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.AccountUpdate_Success_Xpath))
        success_msg = (self.driver.find_element(*EditAccount_AM_Page.AccountUpdate_Success_Xpath)).text
        if success_msg == "Account updated successfully":
            print("Test Case Is Pass")
            return "EditAccount_Pass"
        else:
            print("Test Case Is Fail")
            return "EditAccount_Fail"
