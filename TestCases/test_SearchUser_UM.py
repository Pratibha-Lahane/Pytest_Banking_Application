import time

from PageObject.LoginPage import LoginPage_class
from PageObject.SearchUser_UM_Page import SearchUser_UM_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_Search_user_UM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_search_user_UM_TC007(self, setup):
        self.log.info("Test Case_User-Management-search_user_TC007 is Started-->>")
        self.driver = setup
        self.log.info("Opening Browser-->>")
        self.log.info("To Call LoginPage_Object Create Variable.")
        self.lp = LoginPage_class(self.driver)
        time.sleep(5)
        self.log.info("Click on Login-->>")
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Entering Username-->>")
        self.lp.Enter_Username(self.Username)
        time.sleep(3)
        self.log.info("Entering Password-->>")
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Clicking on Login Button-->>")
        self.lp.Click_On_Login_Button()
        time.sleep(3)
        self.log.info("To call SearchUser_Page_Object Create Variable")
        self.us = SearchUser_UM_class(self.driver)
        time.sleep(5)
        self.log.info("Click On User Management Tab-->>")
        self.us.Click_UserManagement()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.log.info("Entering Username-->>")
        self.us.Entering_Username(self.Username)
        time.sleep(3)
        self.log.info("Clicking on Search user button-->>")
        self.us.Click_Search_User()
        time.sleep(3)

        if self.us.Validate_Search_User() == "Search_User Pass":
            self.log.info("Taking Screenshot-->>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_UM_Search_User_TC007_Pass.png")
            self.log.info("test_UM_search_user_TC007_Is_Pass.")
            self.log.info("<<<-----TestCase BankApp User Management-Search User TC007 Is  Run Successfully----->>>\n")
            assert True
        else:
            self.log.info("Taking Screenshot-->>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_UM_Search_User_TC007_Fail.png")
            self.log.info("test_UM_search_user_TC007 is Fail.")
            self.log.info("<<<-----TestCase BankApp User Management-Search User TC007 Is  Failed..----->>>\n")
            assert False
        self.driver.quit()



