from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SearchUser_UM_class:
    Click_UserManagement_Xpath = (By.XPATH, "//a[normalize-space()='User Management']")
    Text_Username_Xpath = (By.XPATH, "//input[@id='username']")
    Click_Search_User_Button_Xpath = (By.XPATH, "//button[@type='submit']")
    Validate_Search_User_Page_Title_Xpath = (By.XPATH, "//h2[normalize-space()='Edit User']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_UserManagement(self):
        self.driver.find_element(*SearchUser_UM_class.Click_UserManagement_Xpath).click()

    def Entering_Username(self, username):
        self.driver.find_element(*SearchUser_UM_class.Text_Username_Xpath).send_keys(username)

    def Click_Search_User(self):
        self.driver.find_element(*SearchUser_UM_class.Click_Search_User_Button_Xpath).click()

    def Validate_Search_User(self):
        title = self.driver.find_element(*SearchUser_UM_class.Validate_Search_User_Page_Title_Xpath).text
        if title == "Edit User":
            return "Search_User Pass"
        else:
            "Search_User Fail"
