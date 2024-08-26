from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search_Account_AM_Page:
    Text_AccountId_Xpath = (By.XPATH, "//input[@id='accountId']")
    Click_SearchAccount_Xpath = (By.XPATH, "//button[@type='submit']")
    Validate_SearchAccount_Xpath = (By.XPATH, "//h2[normalize-space()='Search Account Results']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Entering_AccountId(self, accountid):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_AccountId_Xpath))
        element = self.driver.find_element(*Search_Account_AM_Page.Text_AccountId_Xpath)
        self.driver.execute_Script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(accountid)

    def Clicking_On_SearchAccount_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_SearchAccount_Xpath))
        self.driver.find_element(*Search_Account_AM_Page.Click_SearchAccount_Xpath).click()
        self.driver.execute_Script("window.scrollTo(0, document.body.scrollHeight);")

    def Validate_SearchAccount(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Validate_SearchAccount_Xpath))
        title = self.driver.find_element(*Search_Account_AM_Page.Validate_SearchAccount_Xpath).text
        if title == "Search Account Results":
            print("Test Case Pass")
            return "SearchAccount_Pass"
        else:
            print("Test Case Is Fail")
            return "SearchAccount_Fail"
