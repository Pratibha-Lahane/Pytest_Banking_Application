import time

from PageObject.CreateCustomer_CM_Page import CreateCustomer_CM_Page
from PageObject.CustomerEdit_CM_Page import EditCustomer_CM_Page
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_CustomerEdit_CM_Class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_EditCustomer_CM_TC013(self, setup):
        self.log.info("Test Case Customer Edit CM TC013 Is Started--->>>")
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
        self.log.info("Create Variable cc To Call CreateCustomer Page Objects Methods-->> ")
        self.cc = CreateCustomer_CM_Page(self.driver)
        time.sleep(3)
        self.log.info("Click On Customer Management Tab--->>>")
        self.cc.Click_On_CustomerManagement_Tab()
        time.sleep(3)
        self.log.info("Create Variable ec To Call CustomerEdit Page Objects Methods--->>")
        self.ec = EditCustomer_CM_Page(self.driver)
        time.sleep(3)
        self.log.info("Click On View All Customer--->>>")
        self.ec.Clicking_On_View_All_Customer_List()
        time.sleep(3)
        self.log.info("Click On Edit Button--->>>")
        self.ec.Clicking_On_Edit_Button()
        time.sleep(3)
        self.log.info("Entering New Address--->>>" + "Shivaji Nagar Pune")
        self.ec.Entering_NewAddress("Shivaji Nagar Pune")
        time.sleep(3)
        self.log.info("Click On Save Changes Button--->>>")
        self.ec.Click_On_Save_Changes_Button()
        time.sleep(3)

        self.log.info("Validate Customer Address Updated--->>")
        if self.ec.Validate_CustomerUpdated() == "CustomerEdit_Pass":
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_CustomerEdit_CM_TC013_Is_Pass.png")
            time.sleep(3)
            self.log.info("Click On Logout Button-->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case Customer Edit CM TC013 Is Pass--->>>\n")
            assert True

        else:
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_CustomerEdit_CM_TC013_Is_Fail.png")
            time.sleep(3)
            self.log.info("Click On Logout Button-->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case Customer Edit CM TC013 Is Fail.--->>>\n")
            assert False

        self.log.info("Closing Browser--->>>")
        self.driver.quit()
