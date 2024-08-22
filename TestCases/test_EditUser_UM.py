import time

from PageObject.EditUser_UM_Page import Edit_User_UM_class
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_EditUser_UM_Class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_EditUser_TC009(self, setup):
        self.driver = setup
        self.log.info("Opening Browser...")
        self.lp = LoginPage_class(self.driver)
        self.log.info("Clicking On Login--->>>")
        time.sleep(3)
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Entering Username--->>>")
        self.lp.Enter_Username(self.Username)
        time.sleep(3)
        self.log.info("Entering Password--->>>")
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Click On Login Button")
        self.lp.Click_On_Login_Button()
        time.sleep(4)
        self.eu = Edit_User_UM_class(self.driver)
        self.log.info("Click On User Management Tab--->>")
        time.sleep(4)
        self.eu.Click_UserManagement_tab()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.log.info("Click On View User List Button---->>>")
        self.eu.Click_ViewUser_List()
        time.sleep(4)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")---use in page object
        time.sleep(3)
        self.log.info("Click On Edit User Tab...")
        self.eu.Click_ON_Edit_UserTab()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.log.info("EditUser_phone_number--->>>")
        self.eu.Edit_Phone_Number("5897762157")
        time.sleep(5)

        self.log.info("Click On Save Changes Button--->>>")
        self.eu.Click_On_Save_Changes()
        time.sleep(3)

        self.log.info("Validating EditUser Status--->>>")
        if self.eu.Validate_EditUser_Status() == "Edit_User_Pass":
            time.sleep(3)
            self.log.info("Test Case Edit User TC009 Is Pass...")
            self.log.info("Taking Screenshot..")
            time.sleep(3)
            self.driver.save_screenshot(".\\ScreenShoot\\test_EditUser_TC009_is_Pass.png")
            time.sleep(3)
            self.log.info("Click On LogOut Button--->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            assert True

        else:
            self.log.info("Test Case Edit User TC009 Is Fail...")
            self.log.info("Taking Screenshot..")
            time.sleep(3)
            self.driver.save_screenshot(".\\ScreenShoot\\test_EditUser_TC009_is_Fail.png")
            time.sleep(3)
            self.log.info("Click On LogOut Button--->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            assert False

        self.log.info("Closing Browser...")
        self.driver.quit()



