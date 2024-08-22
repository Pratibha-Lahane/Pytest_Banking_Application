import time
from PageObject.CreateUser_UM_Page import CreateUser_UM_class
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class
import random
import string


class Test_CreateNewUser_UM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_CreateNew_user_UM_TC008(self, setup):
        self.log.info("Test Case_User-Management-search_user_TC008 is Started-->>")
        self.driver = setup
        self.log.info("Opening Browser-->>")
        self.log.info("To Call LoginPage_Object Create Variable.")
        self.lp = LoginPage_class(self.driver)
        self.log.info("To call CreateUser_Page_Object Create Variable")
        self.uc = CreateUser_UM_class(self.driver)
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

        self.log.info("Click On User Management Tab-->>")
        self.uc.Click_UserManagement()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.log.info("Click Create User")
        self.uc.Click_CreateUser()
        time.sleep(3)
        self.log.info("Entering Username-->>" + generate_random_username())
        self.uc.Entering_Username(generate_random_username())
        time.sleep(3)
        self.log.info("Entering Password-->>" + self.Password)
        self.uc.Entering_Password(self.Password)
        time.sleep(3)
        self.log.info("Entering Email-->>" + generate_random_email())
        self.uc.Entering_Email(generate_random_email())
        time.sleep(3)
        self.log.info("Entering Phone-->>" + generate_random_phone_number())
        self.uc.Entering_Phone(generate_random_phone_number())
        time.sleep(3)
        self.log.info("Clicking On Create User Button-->>")
        self.uc.Click_Create_User()
        time.sleep(3)

        if self.uc.Validate_UM_Create_User() == "User_Created Pass":
            self.log.info("TestCase_Create New_user_UM_TC008 is Pass")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application\\ScreenShoot"
                                        "\\TestCase_Create_New_user_UM_TC008_is_Pass.png")
            self.log.info("<<<-----TestCase BankApp User Management-Create New User TC008 Is  Run "
                          "Successfully----->>>\n")
            assert True
        else:
            self.log.info("TestCase_Create New_user_UM_TC008 is Fail")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("C:\\Users\\Komal\\PycharmProjects\\Pytest_Banking_Application\\ScreenShoot"
                                        "\\TestCase_Create_New_user_UM_TC008_is_Fail.png")
            self.log.info("<<<-----TestCase BankApp User Management-Create New User TC008 Is  Failed.----->>>\n")
            assert False

        self.log.info("Closing Browser")
        self.driver.quit()


def generate_random_username(length=6):
    return 'User' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain


def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))
