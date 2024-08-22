import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SignUp_class:
    click_SignUp_Xpath = (By.XPATH, "//a[normalize-space()='Sign Up']")
    Text_Username_Xpath = (By.XPATH, "//input[@id='username']")
    Text_Password_Xpath = (By.XPATH, "//input[@id='password']")
    Text_Email_Xpath = (By.XPATH, "//input[@id='email']")
    Text_Phone_Xpath = (By.XPATH, "//input[@id='phone']")
    Click_Create_User_Css = (By.CSS_SELECTOR, "button[type='submit']")
    Text_Success_msg_Xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_signUp(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_SignUp_Xpath))
        self.driver.find_element(*SignUp_class.click_SignUp_Xpath).click()

    def Entering_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_Xpath))
        self.driver.find_element(*SignUp_class.Text_Username_Xpath).send_keys(username)

    def Entering_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_Xpath))
        self.driver.find_element(*SignUp_class.Text_Password_Xpath).send_keys(password)

    def Entering_Email(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Email_Xpath))
        self.driver.find_element(*SignUp_class.Text_Email_Xpath).send_keys(email)

    def Entering_Phone(self, phone):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Phone_Xpath))
        self.driver.find_element(*SignUp_class.Text_Phone_Xpath).send_keys(phone)

    def Click_Create_User(self):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Create_User_Css))
        self.driver.find_element(*SignUp_class.Click_Create_User_Css).click()

    def Validate_SignUP_UserCreation_Status(self):
        time.sleep(5)
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Success_msg_Xpath))
        Success_msg = self.driver.find_element(*SignUp_class.Text_Success_msg_Xpath).text
        time.sleep(5)
        if Success_msg == "User created successfully":
            time.sleep(3)
            print("User Creation Sign-Up Test Case Is Pass")
            return "SignUp Pass"
        else:
            print("User Creation Sign-Up Test Case Is Fail")
            return "SignUp Fail"




