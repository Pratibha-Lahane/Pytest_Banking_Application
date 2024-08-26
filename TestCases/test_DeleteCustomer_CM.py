from PageObject.CreateCustomer_CM_Page import CreateCustomer_CM_Page
from PageObject.CustomerEdit_CM_Page import EditCustomer_CM_Page
from PageObject.DeleteCustomer_CM_Page import DeleteCustomer_CM_Page
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class
import time


class Test_DeleteCustomer_CM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_DeleteCustomer_CM_TC014(self, setup):
        self.log.info("Test Case Delete Customer CM TC014 Is Started--->>>")
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
        self.log.info("Create Variable dc To Call DeleteCustomer_Page Object Methods-->>")
        self.dc = DeleteCustomer_CM_Page(self.driver)
        time.sleep(3)
        self.log.info("Clicking On Delete Button--->>>")
        self.dc.Clicking_On_Delete_Button()
        time.sleep(3)
        self.log.info("Validate Customer Deleted--->>>")
        if self.dc.Validate_Customer_Deleted() == "Delete_Customer Pass":
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_DeleteCustomer_CM_TC014_Is_Pass.png")
            time.sleep(3)
            self.log.info("Click On Logout Button-->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case Delete Customer CM TC014 Is Pass--->>>\n")
            assert True

        else:
            time.sleep(3)
            self.log.info("Taking Screenshot--->>>")
            self.driver.save_screenshot(".\\ScreenShoot\\TestCase_DeleteCustomer_CM_TC014_Is_Fail.png")
            time.sleep(3)
            self.log.info("Click On Logout Button-->>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case Delete Customer CM TC014 Is Fail.--->>>\n")
            assert False

        self.log.info("Closing Browser--->>>")
        self.driver.quit()
