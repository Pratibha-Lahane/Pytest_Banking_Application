from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Edit_User_UM_class:
    Click_User_Management_Xpath = (By.XPATH, "//a[normalize-space()='User Management']")
    Click_View_UserList_Xpath = (By.XPATH, "//a[normalize-space()='View All Users']")
    Click_EditUser_Button_Xpath = (By.XPATH, "//tbody/tr[7]/td[4]/a[1]")
    Text_Edit_Phone_Xpath = (By.XPATH, "//input[@name='phone']")
    Click_Save_Changes_Xpath = (By.XPATH, "//button[@type='submit']")
    Validate_Success_Msg_Xpath = (By.XPATH, "//div[@class='success-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_UserManagement_tab(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_User_Management_Xpath))
        self.driver.find_element(*Edit_User_UM_class.Click_User_Management_Xpath).click()

    def Click_ViewUser_List(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_View_UserList_Xpath))
        element = self.driver.find_element(*Edit_User_UM_class.Click_View_UserList_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Click_ON_Edit_UserTab(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_EditUser_Button_Xpath))
        element = self.driver.find_element(*Edit_User_UM_class.Click_EditUser_Button_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Edit_Phone_Number(self, phone):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Edit_Phone_Xpath))
        element = self.driver.find_element(*Edit_User_UM_class.Text_Edit_Phone_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(phone)
        # self.driver.find_element(*Edit_User_UM_class.Text_Edit_Phone_Xpath).clear()
        # self.driver.find_element(*Edit_User_UM_class.Text_Edit_Phone_Xpath).Send_keys(phone)

    def Click_On_Save_Changes(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Save_Changes_Xpath))
        self.driver.find_element(*Edit_User_UM_class.Click_Save_Changes_Xpath).click()

    def Validate_EditUser_Status(self):
        Success_msg = (self.driver.find_element(*Edit_User_UM_class.Validate_Success_Msg_Xpath)).text
        print(Success_msg)
        if Success_msg == "User updated successfully":
            print("Edit User Successfully...")
            print("Test Case Edit User Is Pass...")
            return "Edit_User_Pass"

        else:
            print("Test Case Edit User Is Fail...")
            return "Edit_User_Fail"
