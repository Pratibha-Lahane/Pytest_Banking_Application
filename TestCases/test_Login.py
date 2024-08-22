import time

import pytest

from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_BankingApp_Login:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    Log = LogGenerator.loggen()

    @pytest.mark.Login_TestCases
    def test_BankApp_Url_TC001(self, setup):
        self.Log.info("TestCase test_BankApp_URL_TC001 is Started.")
        self.driver = setup
        self.Log.info("Opening Browser--->>>")
        print("driver.title-->>", self.driver.title)
        self.Log.info("Checking Page Title--->>>")
        if self.driver.title == "Bank Application":
            time.sleep(2)
            self.Log.info("Test Case BankApp Url TC001 Is Pass")
            self.Log.info("Taking Screenshot--->>")
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                        "\\ScreenShoot\\TestCase_BankApp_Url_TC001_Pass.png")
            print("<<<-----TestCase BankApp Url TC001 Is  Run Successfully----->>>")
            assert True

        else:
            print("Test Case BankApp Url TC001 Is Pass")
            time.sleep(2)
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                        "\\ScreenShoot\\TestCase_BankApp_Url_TC001_Fail.png")
            print("<<<-----TestCase BankApp Url TC001 Is  Run Successfully----->>>\n")
            assert False
        self.driver.quit()

    def test_BankApp_Login_TC002(self, setup):
        self.Log.info("Test Case BankApp Login TC002 Is Started--->>>")
        self.driver = setup
        self.Log.info("Opening Browser--->>>")
        self.lp = LoginPage_class(self.driver)
        time.sleep(4)
        self.Log.info("self.Username--->>", self.Username)
        self.Log.info("self.Password--->>", self.Password)
        self.Log.info("Clicking On Login--->>>")
        self.lp.Click_Login()
        self.Log.info("Entering Username--->>>")
        self.lp.Enter_Username(self.Username)
        self.Log.info("Entering Password--->>>")
        self.lp.Enter_Password(self.Password)
        self.Log.info("Click On Login Button")
        self.lp.Click_On_Login_Button()
        time.sleep(4)
        self.Log.info("Validating Login Status--->>>")

        if self.lp.Validate_Login_Status() == "LoginPass":
            time.sleep(4)
            self.Log.info("Test Case BankApp Login TC002 Is Pass")
            time.sleep(4)
            self.Log.info("<<--Login Successfully With Valid Credentials and Redirecting To BankApp HomePage-->>\n")
            self.Log.info("Taking ScreenShot---->>>")
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                        "\\ScreenShoot\\TestCase_BankApp_Login_TC002_Pass.png")
            self.Log.info("<<<-----TestCase BankApp Login TC002 Is  Run Successfully----->>>\n")
            self.Log.info("Click On LogOut Button--->>")
            self.lp.Click_On_LogOut_Button()
            assert True
        else:
            self.Log.info("Test Case BankApp Login TC002 Is Fail")
            time.sleep(2)
            self.Log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                        "\\ScreenShoot\\TestCase_BankApp_Login_TC002_Fail.png")
            self.Log.info("<<<-----TestCase BankApp Login TC002 Is  Run Successfully----->>>\n")
            assert False
        self.driver.quit()
