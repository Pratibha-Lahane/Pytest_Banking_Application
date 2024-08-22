import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage_class:
    Click_Login_Css = (By.CSS_SELECTOR, "body > div:nth-child(1) > nav:nth-child(5) > ul:nth-child(1) > "
                                        "li:nth-child(2) > a:nth-child(1)")
    Text_UserName_XPATH = (By.XPATH, "//input[@id='username']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    HomePage_Menu_XPATH = (By.XPATH, "//h2[normalize-space()='Dashboard']")
    click_Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def Click_Login(self):
        # self.wait.until(expected_conditions.invisibility_of_element_located(self.Click_Login_Css))
        self.driver.find_element(*LoginPage_class.Click_Login_Css).click()

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_UserName_XPATH))
        self.driver.find_element(*LoginPage_class.Text_UserName_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_XPATH))
        self.driver.find_element(*LoginPage_class.Text_Password_XPATH).send_keys(password)

    def Click_On_Login_Button(self):
        self.driver.find_element(*LoginPage_class.Click_Login_Button_XPATH).click()

    def Click_On_LogOut_Button(self):
        self.driver.find_element(*LoginPage_class.click_Logout_Button_XPATH).click()

    def Validate_Login_Status(self):
        try:
            time.sleep(2)
            self.driver.find_element(*LoginPage_class.HomePage_Menu_XPATH)
            time.sleep(2)
            print("User login test case is passed")
            return "LoginPass"
        except:
            print("User login test case is failed")
            return "LoginFail"
