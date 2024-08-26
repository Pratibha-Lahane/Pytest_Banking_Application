import time

from PageObject.CreateAccount_AM_Page import CreateAccount_AM_Page
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_CreateAccount_AM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_CreateAccount_AM_TC015(self, setup):
        self.log.info("Test Case Create Account AM TC015 Is Started--->>>")
        time.sleep(3)
        self.driver = setup
        self.log.info("Opening Browser--->>>")
        time.sleep(3)
        self.log.info("Create Variable lp To Call LoginPage Objects Methods--->>>")
        self.lp = LoginPage_class(self.driver)
        time.sleep(3)
        self.log.info("Click On Login Tab--->>")
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Entering Username-->>" + self.Username)
        self.lp.Enter_Username(self.Username)
        time.sleep(3)
        self.log.info("Entering Password--->>>" + self.Password)
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Click On Login Button-->>")
        self.lp.Click_On_Login_Button()
        time.sleep(3)
        self.log.info("create variable ca To call Create Account AM Page Object Method--->>")
        self.ca = CreateAccount_AM_Page(self.driver)
        self.log.info("Click On Account Management---->>>")
        self.ca.Clicking_On_AccountManagement_Tab()
        self.log.info("")