import time

import pytest

from PageObject.LoginPage import LoginPage_class
from Utilities import XLUtils
from Utilities.Logger import LogGenerator


# from Utilities.readConfigFile import ReadConfig_class


class Test_BankingApp_Login:
    File_Path = ("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application\\"
                 "TestCases\\TestData\\BankApp_Login_TestData.xlsx")
    log = LogGenerator.loggen()

    @pytest.mark.Login_TestCases
    def test_BankApp_Login_DDTest_TC003(self, setup):
        self.log.info("test_BankApp_Login_DDTest_TC003 Is Started--->>>")
        self.driver = setup
        self.log.info("Opening Browser--->>>")
        self.lp = LoginPage_class(self.driver)
        time.sleep(4)
        self.log.info("Checking Row Count from Excel--->>")
        self.rows = XLUtils.getRowCount(self.File_Path, "Login_TestData")
        print("Number of rows in Excel Test data-->" + str(self.rows))
        self.log.info("Prepared Empty List--->>>")
        List_Status = []
        time.sleep(2)
        self.log.info("Clicking On Login--->>>")
        self.lp.Click_Login()
        time.sleep(3)
        self.log.info("Checking All Loops-->>>")
        for r in range(2, self.rows + 1):
            time.sleep(5)
            self.log.info("Reading Username From Excel--->>>")
            self.username = XLUtils.readData(self.File_Path, "Login_TestData", r, 2)
            self.log.info("Reading Password From Excel--->>>")
            self.password = XLUtils.readData(self.File_Path, "Login_TestData", r, 3)
            self.log.info("Reading Expected Results From Excel--->>>")
            self.Expected_Results = XLUtils.readData(self.File_Path, "Login_TestData", r, 4)
            self.log.info("username-->" + "loop-->" + str(r) + "--" + str(self.username))
            self.log.info("password-->" + "loop-->" + str(r) + "--" + str(self.password))
            self.log.info("Expected_Result-->" + "loop-->" + str(r) + "--" + str(self.Expected_Results))
            self.log.info("---------------------\n")
            self.log.info("Entering Username--->>>", self.username)
            self.lp.Enter_Username(self.username)
            time.sleep(2)
            self.log.info("Entering Password--->>>", self.password)
            self.lp.Enter_Password(self.password)
            time.sleep(2)
            self.log.info("Clicking On Login Button--->>>")
            self.lp.Click_On_Login_Button()
            time.sleep(4)

            self.log.info("Validating Login Status--->>>")
            if self.lp.Validate_Login_Status() == "LoginPass" and self.Expected_Results == "Login_Pass":
                time.sleep(4)
                self.log.info("Append Login Status Into List_Status--->>>")
                List_Status.append("Pass")
                self.log.info("Writing Actual Login Status Into Excel Sheet--->>")
                XLUtils.writeData(self.File_Path, "Login_TestData", r, 5, "Pass")
                time.sleep(4)
                self.log.info("Tanking Screenshot--->>>")
                self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                            "\\ScreenShoot\\TestCase_BankApp_LoginDDTest_TC1.1_Pass.png")
                self.log.info("Test Case BankApp LoginDDTest TC003 Is Pass")
                self.log.info("Login Successfully With Valid Credentials and Redirecting To BankApp HomePage-->>\n")
                self.log.info("Clicking On LogOut Button--->>>")
                self.lp.Click_On_LogOut_Button()

                self.log.info("Validating Login Status--->>>")
            elif self.lp.Validate_Login_Status() == "LoginPass" and self.Expected_Results == "Login_Fail":
                time.sleep(4)
                self.log.info("Append Login Status Into List_Status--->>>")
                List_Status.append("Fail")
                self.log.info("Writing Actual Login Status Into Excel Sheet--->>")
                XLUtils.writeData(self.File_Path, "Login_TestData", r, 5, "Fail")
                time.sleep(4)
                self.log.info("Taking Screenshot--->>")
                self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                            "\\ScreenShoot\\TestCase_BankApp_LoginDDTest_TC003_Fail.png")
                self.log.info("Test Case BankApp LoginDDTest TC003 Is Fail")

                self.log.info("Validating Login Status--->>>")
            elif self.lp.Validate_Login_Status() == "LoginFail" and self.Expected_Results == "Login_Pass":
                time.sleep(4)
                self.log.info("Append Login Status Into List_Status--->>>")
                List_Status.append("Fail")
                self.log.info("Writing Actual Login Status Into Excel Sheet--->>")
                XLUtils.writeData(self.File_Path, "Login_TestData", r, 5, "Fail")
                time.sleep(4)
                self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                            "\\ScreenShoot\\TestCase_BankApp_LoginDDTest_TC003_Fail.png")
                self.log.info("Test Case BankApp LoginDDTest TC003 Is Fail")

                self.log.info("Validating Login Status--->>>")
            elif self.lp.Validate_Login_Status() == "LoginFail" and self.Expected_Results == "Login_Fail":
                time.sleep(4)
                self.log.info("Append Login Status Into List_Status--->>>")
                List_Status.append("Pass")
                self.log.info("Writing Actual Login Status Into Excel Sheet--->>")
                XLUtils.writeData(self.File_Path, "Login_TestData", r, 5, "Pass")
                time.sleep(4)
                self.log.info("Taking Screenshot-->>>")
                self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                                            "\\ScreenShoot\\TestCase_BankApp_LoginDDTest_TC003_Pass.png")
                self.log.info("Test Case BankApp LoginDDTest TC003 Is Pass\n")

        print("Testcase pass count-->" + str(List_Status.count("pass")))
        print("Testcase fail count-->" + str(List_Status.count("fail")))
        self.log.info("Login Status List--->>>")
        print(List_Status)
        self.log.info("Validating List Status--->>>")
        if "Fail" not in List_Status:
            self.log.info("test_BankingApp_Login_DDT_TC003 is passed")
            self.log.info("<<<-----TestCase BankApp LoginDDTest TC003 Is  Run Successfully----->>>\n")
            assert True
        else:
            self.log.info("test_BankingApp_Login_DDT_TC003 is failed")
            self.log.info("<<<-----TestCase BankApp LoginDDTest TC003 Is  Failed----->>>\n")
            assert False

        self.log.info("Closing Browser--->>>")
        self.driver.quit()  # Close the browser
