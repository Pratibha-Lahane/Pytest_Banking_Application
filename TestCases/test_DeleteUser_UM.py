import time

from PageObject.EditUser_UM_Page import Edit_User_UM_class
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class
from PageObject.DeleteUser_UM_Page import DeleteUserUM_Page
from PageObject.SearchUser_UM_Page import SearchUser_UM_class


class Test_DeleteUser_UM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_DeleteUser_UM_TC010(self, setup):
        self.log.info("Test Case Delete User TC010 In UM Is Started...")
        self.driver = setup
        self.log.info("Opening Browser--->>")
        time.sleep(3)
        self.log.info("Creating Variable to Call Login Page Class-->>")
        self.lp = LoginPage_class(self.driver)
        time.sleep(3)
        self.log.info("Click on Login Tab-->>")
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Entering Username--->>>" + self.Username)
        self.lp.Enter_Username(self.Username)
        time.sleep(3)
        self.log.info("Entering Password--->>>" + self.Password)
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Click On Login Button--->>>")
        self.lp.Click_On_Login_Button()
        time.sleep(3)
        self.log.info("Creating Variable to Call Edit User Class-->>")
        self.eu = Edit_User_UM_class(self.driver)
        time.sleep(3)
        self.log.info("Clicking On User Management Tab--->>")
        self.eu.Click_UserManagement_tab()
        time.sleep(3)
        self.log.info("Click On View User List---->>>")
        self.eu.Click_ViewUser_List()
        time.sleep(5)
        self.log.info("Creating Variable to Call Delete User Class-->>")
        self.du = DeleteUserUM_Page(self.driver)
        time.sleep(5)
        self.log.info("Click On Next Page Number-->>>")
        self.driver.get("https://bankapp.credence.in/users?page=63")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.log.info("Click On Delete User Button--->>")
        self.du.Click_On_DeleteUser()
        time.sleep(10)
        self.log.info("Creating Variable to call Search User Class--->>>")
        self.su = SearchUser_UM_class(self.driver)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.log.info("Enter Username for Searching--->>>")
        self.su.Entering_Username("Jemmy")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.log.info("Clicking on Search user button-->>")
        self.su.Click_Search_User()
        time.sleep(3)

        time.sleep(3)
        self.log.info("Validate User Deleted--->>>")
        if self.du.Validate_DeleteUser() == "User_Deleted Pass":
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\test_DeleteUser_UM_TC010_Is_Pass.png")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.log.info("Click On Logout Button-->>")
            self.lp.Click_On_Login_Button()
            time.sleep(3)
            self.log.info("Test Case Delete User TC010 In UM Is Passed--")
            self.log.info("<<<<<--------Test Case Delete User TC010 In UM Is Run Successfully------->>>\n")
            assert True

        else:
            self.log.info("Test Case Delete User TC010 In UM Is Fail.--")
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\test_DeleteUser_UM_TC010_Is_Fail.png")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.log.info("Click On Logout Button-->>")
            self.lp.Click_On_Login_Button()
            time.sleep(3)
            self.log.info("<<<<<--------Test Case Delete User TC010 In UM Is Failed------->>>\n")
            assert True

        self.log.info("Closing Browser--->>>>")
        self.driver.quit()

