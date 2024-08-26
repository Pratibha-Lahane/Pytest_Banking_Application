from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class CreateAccount_AM_Page:
    Click_AccountManagement_Xpath = (By.XPATH, "//a[normalize-space()='Account Management']")
    Click_On_CreateAccount_Xpath = (By.XPATH, "//a[normalize-space()='Create Account']")
    Text_CustomerId_Xpath = (By.XPATH, "//input[@id='customerId']")
    select_AccountType_Xpath = (By.XPATH, "//select[@id='accountTypeId']")
    Text_Balance_Xpath = (By.XPATH, "//input[@id='balance']")
    Click_CreateAccount_Button = (By.XPATH, "//button[@type='submit']")
    Validate_Success_Msg_Xpath = (By.XPATH, "//div[@class='success-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clicking_On_AccountManagement_Tab(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_AccountManagement_Xpath))
        element = self.driver.find_element(*CreateAccount_AM_Page.Click_AccountManagement_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Click_On_CreateAccount(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_On_CreateAccount_Xpath))
        element = self.driver.find_element(*CreateAccount_AM_Page.Click_AccountManagement_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Entering_CustomerId(self, customerid):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_CustomerId_Xpath))
        element = self.driver.find_element(*CreateAccount_AM_Page.Text_CustomerId_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(customerid)

    def Select_AccountTypes(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.select_AccountType_Xpath))
        Select(self.driver.find_element(*CreateAccount_AM_Page.select_AccountType_Xpath)).select_by_index(1)

    def Entering_Balance(self, balance):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Balance_Xpath))
        self.driver.find_element(*CreateAccount_AM_Page.Text_Balance_Xpath).send_keys(balance)

    def Click_Create_Account_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_CreateAccount_Button))
        self.driver.find_element(*CreateAccount_AM_Page.Click_CreateAccount_Button).click()

    def Validate_AccountCreated(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Validate_Success_Msg_Xpath))
        success_msg = (self.driver.find_element(*CreateAccount_AM_Page.Validate_Success_Msg_Xpath)).text
        if success_msg == "Account created successfully":
            print("Test Case Is Pass")
            return "AccountCreated_Pass"
        else:
            print("Test Case Is Fail")
            return "AccountCreated_Fail"
