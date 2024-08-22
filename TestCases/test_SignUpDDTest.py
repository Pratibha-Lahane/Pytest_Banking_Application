import time

import pytest

from PageObject.SignUp_Page import SignUp_class
from Utilities import XLUtils
from Utilities.Logger import LogGenerator


class Test_SignUp_DDT_class:
    file_path = ("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application"
                 "\\TestCases\\TestData\\BankApp_SignUp_TestData.xlsx")
    log = LogGenerator.loggen()

    @pytest.mark.SignUp_TestCases
    def test_signup_DDTest_TC006(self, setup):
        self.log.info("Test Case Sign Up DDT TC006 Is Started...")
        self.driver = setup
        self.log.info("Opening Browser-->>")
        self.log.info("Creating Variable to call SignUp_class from SignUp PageObject....")
        self.su = SignUp_class(self.driver)
        self.log.info("Clicking On Sign Up--->>>")
        self.su.click_signUp()
        self.log.info("Checking Row Count From Excel--->>")
        self.rows = XLUtils.getRowCount(self.file_path, sheet_name="SignUp_TestData")
        print("number of rows in excel sheet data-->>" + str(self.rows))
        self.log.info("Prepare Empty List--->>")
        SignUp_List_Status = []
        self.log.info("Verifying All Loops--->>>")
        for r in range(2, self.rows + 1):
            time.sleep(3)
            self.log.info("Reading Username from Excel sheet--->>")
            self.username = XLUtils.readData(self.file_path, "SignUp_TestData", r, 2)
            self.log.info("Reading Password from Excel sheet--->>")
            self.password = XLUtils.readData(self.file_path, "SignUp_TestData", r, 3)
            self.log.info("Reading Email from Excel sheet--->>")
            self.email = XLUtils.readData(self.file_path, "SignUp_TestData", r, 4)
            self.log.info("Reading Phone from Excel sheet--->>")
            self.phone = XLUtils.readData(self.file_path, "SignUp_TestData", r, 5)
            self.log.info("Reading Expected_Results from Excel sheet--->>")
            self.Expected_Results = XLUtils.readData(self.file_path, "SignUp_TestData", r, 6)
            self.log.info("username-->" + "loop-->" + str(r) + "--" + str(self.username))
            self.log.info("password-->" + "loop-->" + str(r) + "--" + str(self.password))
            self.log.info("email-->" + "loop-->" + str(r) + "--" + str(self.email))
            self.log.info("phone-->" + "loop-->" + str(r) + "--" + str(self.phone))
            self.log.info("Expected_Result-->" + "loop-->" + str(r) + "--" + str(self.Expected_Results))
            self.log.info("---------------------\n")
            self.log.info("Entering Username-->>" + self.username)
            self.su.Entering_Username(self.username)
            time.sleep(2)
            self.log.info("Entering Password-->>" + self.password)
            self.su.Entering_Password(self.password)
            time.sleep(3)
            self.log.info("Entering Email--->>" + self.email)
            self.su.Entering_Email(self.email)
            time.sleep(3)
            self.log.info("Entering Phone-->>")
            self.su.Entering_Phone(self.phone)
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.log.info("Clicking On Create User In SignUp-->>")
            self.su.Click_Create_User()
            time.sleep(5)

            self.log.info("validating User Create in sign up status-->>")
            if self.su.Validate_SignUP_UserCreation_Status() == "SignUp Pass" and self.Expected_Results == "SignUp_Pass":
                time.sleep(3)
                self.log.info("Append SignUp Status Into SignUp_List_Status--->>")
                SignUp_List_Status.append("Pass")
                self.log.info("Writing Actual SignUp Status Into Excel Sheet-->>")
                XLUtils.writeData(self.file_path, "SignUp_TestData", r, 7, "TC_Pass")
                self.log.info("Taking Screenshot-->>")
                self.driver.save_screenshot(".\\ScreenShoot\\test_signup_DDTest_TC006_Is_Pass.png")
                self.log.info("Test Case SignUp DDT TC006 Is Pass.\n")

            elif self.su.Validate_SignUP_UserCreation_Status() == "SignUp Pass" and self.Expected_Results == "SignUp_Fail":
                time.sleep(3)
                self.log.info("Append SignUp Status Into SignUp_List_Status--->>")
                SignUp_List_Status.append("Fail")
                self.log.info("Writing Actual SignUp Status Into Excel Sheet-->>")
                XLUtils.writeData(self.file_path, "SignUp_TestData", r, 7, "TC_Fail")
                self.log.info("Taking Screenshot-->>")
                self.driver.save_screenshot(".\\ScreenShoot\\test_signup_DDTest_TC006_Is_Fail.png")
                self.log.info("Test Case SignUp DDT TC006 Is Fail.\n")

            elif self.su.Validate_SignUP_UserCreation_Status() == "SignUp Fail" and self.Expected_Results == "SignUp_Pass":
                time.sleep(3)
                self.log.info("Append SignUp Status Into SignUp_List_Status--->>")
                SignUp_List_Status.append("Fail")
                self.log.info("Writing Actual SignUp Status Into Excel Sheet-->>")
                XLUtils.writeData(self.file_path, "SignUp_TestData", r, 7, "TC_Fail")
                self.log.info("Taking Screenshot-->>")
                self.driver.save_screenshot(".\\ScreenShoot\\test_signup_DDTest_TC006_Is_Fail.png")
                self.log.info("Test Case SignUp DDT TC006 Is Fail.\n")

            elif self.su.Validate_SignUP_UserCreation_Status() == "SignUp Fail" and self.Expected_Results == "SignUp_Fail":
                time.sleep(3)
                self.log.info("Append SignUp Status Into SignUp_List_Status--->>")
                SignUp_List_Status.append("Pass")
                self.log.info("Writing Actual SignUp Status Into Excel Sheet-->>")
                XLUtils.writeData(self.file_path, "SignUp_TestData", r, 7, "TC_Pass")
                self.log.info("Taking Screenshot-->>")
                self.driver.save_screenshot(".\\ScreenShoot\\test_signup_DDTest_TC006_Is_Pass.png")
                self.log.info("Test Case SignUp DDT TC006 Is Pass.\n")

        print("Number Of Pass Count In SignUp_List Status-->> ", SignUp_List_Status.count("Pass"))
        print("Number Of Pass Count In SignUp_List Status-->> ", SignUp_List_Status.count("Pass"))
        print(SignUp_List_Status)
        self.log.info("Validating SignUp_List Status--->>>")
        if "Fail" not in SignUp_List_Status:
            self.log.info("Test Case SignUp DDT TC006 Is Pass.")
            self.log.info("<<<-----TestCase BankApp SignUp DDTest TC006 Is  Run Successfully----->>>\n")
            assert True
        else:
            self.log.info("test_BankingApp_SignUP_DDT_TC006 is failed")
            self.log.info("<<<-----TestCase BankApp SighUp DDTest TC006 Is  Failed----->>>\n")
            assert False

        self.log.info("Closing Browser--->>>")
        self.driver.quit()  # Close the browser
