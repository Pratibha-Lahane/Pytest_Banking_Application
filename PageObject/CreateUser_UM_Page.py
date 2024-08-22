from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CreateUser_UM_class:
    Click_UserManagement_Xpath = (By.XPATH, "//a[normalize-space()='User Management']")
    click_CreateUser_Xpath = (By.XPATH, "//a[normalize-space()='Create User']")
    Text_Username_Xpath = (By.XPATH, "//input[@id='username']")
    Text_Password_Xpath = (By.XPATH, "//input[@id='password']")
    Text_Email_Xpath = (By.XPATH, "//input[@id='email']")
    Text_Phone_Xpath = (By.XPATH, "//input[@id='phone']")
    Click_CreateUser_Button_Xpath = (By.XPATH, "//button[normalize-space()='Create User']")
    Validate_Success_msg_Xpath = (By.XPATH, "//div[@class='success-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_UserManagement(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_UserManagement_Xpath))
        self.driver.find_element(*CreateUser_UM_class.Click_UserManagement_Xpath).click()

    def Click_CreateUser(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_CreateUser_Xpath))
        self.driver.find_element(*CreateUser_UM_class.click_CreateUser_Xpath).click()

    def Entering_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_Xpath))
        self.driver.find_element(*CreateUser_UM_class.Text_Username_Xpath).clear()
        self.driver.find_element(*CreateUser_UM_class.Text_Username_Xpath).send_keys(username)

    def Entering_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_Xpath))
        self.driver.find_element(*CreateUser_UM_class.Text_Password_Xpath).clear()
        self.driver.find_element(*CreateUser_UM_class.Text_Password_Xpath).send_keys(password)

    def Entering_Email(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Email_Xpath))
        self.driver.find_element(*CreateUser_UM_class.Text_Email_Xpath).send_keys(email)

    def Entering_Phone(self, phone):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Phone_Xpath))
        self.driver.find_element(*CreateUser_UM_class.Text_Phone_Xpath).send_keys(phone)

    def Click_Create_User(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_CreateUser_Xpath))
        self.driver.find_element(*CreateUser_UM_class.Click_CreateUser_Button_Xpath).click()

    def Validate_UM_Create_User(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Validate_Success_msg_Xpath))

        title = self.driver.find_element(*CreateUser_UM_class.Validate_Success_msg_Xpath).text
        if title == "User created successfully":
            return "User_Created Pass"
        else:
            "User_Created Fail"
