import time

from PageObject.LoginPage import LoginPage_class

from Utilities.Logger import LogGenerator


class Test_BankApp_Login_Params:
    log = LogGenerator.loggen()

    def test_BankApp_Login_Params_TC004(self, setup, getDataForLogin):
        self.log.info("Test Case BankApp Login Params TC004 Started....")
        self.driver = setup
        time.sleep(3)
        self.log.info("Opening Browser--->>>")
        self.log.info("Create Variable to call LoginPage Object Class-->>")
        self.lp = LoginPage_class(self.driver)
        time.sleep(3)
        self.log.info("Create Variable For Login Test Data")
        self.Username = getDataForLogin[0]
        self.Password = getDataForLogin[1]
        Expected_results = getDataForLogin[2]
        # self.log.info("Username-->>", self.Username)
        # self.log.info("Password-->>",)
        # self.log.info("Login_Status-->>", self.Password)
        time.sleep(3)
        self.log.info("click on Login Tab--->>")
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Entering Username--->>>" + self.Username)
        self.lp.Enter_Username(self.Username)
        time.sleep(3)
        self.log.info("Entering Password--->>>" + self.Password)
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Clicking On Login Button--->>")
        self.lp.Click_On_Login_Button()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.log.info("Validating Login Status--->>>")
        if self.lp.Validate_Login_Status() == "LoginPass" and Expected_results == "LoginPass":
            time.sleep(3)
            self.log.info("<<--Login Successfully With Valid Credentials and Redirecting To BankApp HomePage-->>")
            self.log.info("Taking Screenshot---->>>")
            time.sleep(3)
            self.driver.save_screenshot(".\\ScreenShoot\\Test_Case_BankApp_Login_Params_"
                                        "With_Valid_Credentials_TC004_Is_Pass.png")
            time.sleep(3)
            self.log.info("Click On LogOut Button--->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case BankApp Login Params TC004 Is Pass..\n")

        elif self.lp.Validate_Login_Status() == "LoginPass" and Expected_results == "LoginFail":
            time.sleep(3)
            self.log.info("Taking Screenshot---->>>")
            time.sleep(3)
            self.driver.save_screenshot(".\\ScreenShoot\\Test_Case_BankApp_Login_Params_TC004_Is_Fail.png")
            time.sleep(3)
            self.log.info("Test Case BankApp Login Params TC004 Is Fail..\n")

        elif self.lp.Validate_Login_Status() == "LoginFail" and Expected_results == "LoginPass":
            time.sleep(3)
            self.log.info("Taking Screenshot---->>>")
            time.sleep(3)
            self.driver.save_screenshot(".\\ScreenShoot\\Test_Case_BankApp_Login_Params_TC004_Is_Fail.png")
            time.sleep(3)
            self.log.info("Test Case BankApp Login Params TC004 Is Fail..\n")

        elif self.lp.Validate_Login_Status() == "LoginFail" and Expected_results == "LoginFail":
            time.sleep(3)
            self.log.info("<<--Test Case Login Params Fail To Login With Invalid Credentials-->>")
            self.log.info("Taking Screenshot---->>>")
            time.sleep(3)
            self.driver.save_screenshot(".\\ScreenShoot\\Test_Case_BankApp_Login_Params_TC004_Is_Pass.png")
            time.sleep(3)
            self.log.info("Test Case BankApp Login Params TC004 Is Pass..\n")

        self.log.info("Closing Browser")
        self.driver.quit()
