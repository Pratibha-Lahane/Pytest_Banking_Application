import random
import string
import time

import pytest

from PageObject.SignUp_Page import SignUp_class
from Utilities.Logger import LogGenerator


class Test_SignUp:
    log = LogGenerator.loggen()

    @pytest.mark.SignUp_TestCases
    def test_Signup_005(self, setup):
        self.log.info("Test Case User_Creation SignUp TC005 Is Started..")
        self.driver = setup
        self.log.info("Opening Browser-->>")
        self.su = SignUp_class(self.driver)
        self.log.info("click on sign up-->>")
        self.su.click_signUp()
        self.log.info("Entering Username -->>" + generate_random_username())
        self.su.Entering_Username(generate_random_username())
        self.log.info("Entering Password--->>" + "Admin@234")
        self.su.Entering_Password("Admin@234")
        self.log.info("Entering Email -->>" + generate_random_email())
        self.su.Entering_Email(generate_random_email())
        self.log.info("Entering Phone--->>" + generate_random_phone_number())
        self.su.Entering_Phone(generate_random_phone_number())
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.log.info("Clicking on Create User--->>")
        self.su.Click_Create_User()
        time.sleep(10)

        self.log.info("validating User Create in sign up status-->>")

        if self.su.Validate_SignUP_UserCreation_Status() == "SignUp Pass":
            # print(self.su.Validate_SignUP_UserCreation_Status())
            time.sleep(5)
            self.log.info(" Test Case TC005 User Creation In SignUp Is Pass")
            self.log.info("Taking Screenshot")
            time.sleep(5)
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application\\ScreenShoot\\"
                                        "TestCase_TC005_UserCreation_In_SignUp_Is_Pass.png")
            self.log.info("<<<-----TestCase BankApp UserCreation In SignUp TC005 Is  Run Successfully----->>>\n")
            assert True
        else:
            time.sleep(5)
            self.log.info(" Test Case TC005 User Creation In SignUp Is Fail")
            self.log.info("Taking Screenshot")
            time.sleep(5)
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application\\ScreenShoot\\"
                                        "TestCase_TC005_UserCreation_In_SignUp_Is_Fail.png")
            self.log.info("<<<-----TestCase BankApp UserCreation In SignUp TC005 Is  Completed.----->>>\n")
            assert False
        self.driver.quit()


def generate_random_username(length=6):
    return 'Admin' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain


def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))
