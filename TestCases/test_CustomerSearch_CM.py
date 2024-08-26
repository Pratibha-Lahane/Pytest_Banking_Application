import time

from PageObject.CreateCustomer_CM_Page import CreateCustomer_CM_Page
from PageObject.CustomerSearch_CM_Page import CustomerSearch_CM_Page
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_CustomerSearch_CM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_CustomerSearch_CM_TC012(self, setup):
        self.log.info("Test Case Customer Search CM TC012 Is Started--->>>>")
        time.sleep(3)
        self.driver = setup
        self.log.info("Opening Browser--->>>")
        time.sleep(3)
        self.log.info("Create Variable 'lp' To Call Login Page Object Methods--->>")
        self.lp = LoginPage_class(self.driver)
        self.log.info("Click Login Tab-->>")
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Entering Username-->>" + self.Username)
        self.lp.Enter_Username(self.Username)
        time.sleep(3)
        self.log.info("Entering Password--->>" + self.Password)
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Click On Login Button-->>")
        self.lp.Click_On_Login_Button()
        time.sleep(3)
        self.log.info("Create Variable 'cc' To Call CreateCustomer_Page object Methods--->>")
        self.cc = CreateCustomer_CM_Page(self.driver)
        time.sleep(3)
        self.log.info("Click On Customer Management Tab--->>>")
        self.cc.Click_On_CustomerManagement_Tab()
        time.sleep(3)
        self.log.info("Create Variable 'sc' To Call CustomerSearch_CM Page Object Methods--->>")
        self.cs = CustomerSearch_CM_Page(self.driver)
        time.sleep(3)
        self.log.info("Entering CustomerID--->>>" + "242")
        self.cs.Entering_CustomerID("242")
        time.sleep(3)
        self.log.info("Click On SearchCustomer Button --->>>")
        self.cs.Click_On_SearchCustomer()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(3)
        self.log.info("Validate Customer Search--->>")
        if self.cs.Validate_SearchCustomer() == "Customer_Search Pass.":
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_CustomerSearch_CM_TC012_Is_Pass.png")
            time.sleep(3)
            self.log.info("Click On LogOut Button--->>>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("<<<----Test Case Customer Search CM TC012 Is Pass---->>\n")
            assert True

        else:
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_CustomerSearch_CM_TC012_Is_Fail.png")
            time.sleep(3)
            self.log.info("Click On LogOut Button--->>>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("<<<----Test Case Customer Search CM TC012 Is Fail---->>\n")
            assert False

        self.log.info("Closing Browser--->>>")
        self.driver.quit()
