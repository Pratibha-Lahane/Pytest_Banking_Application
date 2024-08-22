import time

from PageObject.CreateCustomer_CM_Page import CreateCustomer_CM_Page
from PageObject.LoginPage import LoginPage_class
from Utilities.Logger import LogGenerator
from Utilities.readConfigFile import ReadConfig_class


class Test_CreateNewCustomer_CM_class:
    Username = ReadConfig_class.getUsername()
    Password = ReadConfig_class.getPassword()
    log = LogGenerator.loggen()

    def test_CreateNewCustomer_TC011(self, setup):
        self.log.info("Test Case Create New Customer TC011 In CM Is Started---->>>")
        self.driver = setup
        self.log.info("opening Browser--->>")
        time.sleep(4)
        self.log.info("Create Variable lp to call LoginPage Methods-->>")
        self.lp = LoginPage_class(self.driver)
        self.log.info("Click Login Tab-->>")
        self.lp.Click_Login()
        time.sleep(4)
        self.log.info("Entering Username--->>" + self.Username)
        self.lp.Enter_Username(self.Username)
        time.sleep(4)
        self.log.info("Entering Password--->>" + self.Password)
        self.lp.Enter_Password(self.Password)
        time.sleep(4)
        self.log.info("Click On Login Button-->>")
        self.lp.Click_On_Login_Button()
        time.sleep(4)
        self.log.info("Create Variable cc To Call CreateCustomer Page Object Methods-->>")
        self.cc = CreateCustomer_CM_Page(self.driver)
        time.sleep(4)
        self.log.info("Click On Customer Management Tab--->>")
        self.cc.Click_On_CustomerManagement_Tab()
        time.sleep(4)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        # time.sleep(2)
        self.log.info("Click On Create Customer-->>")
        self.cc.Click_CreateCustomer()
        time.sleep(4)
        self.log.info("Entering UserId--->>" + "307")
        self.cc.Entering_UserId("307")
        time.sleep(4)
        self.log.info("Entering Firstname--->>" + "Jessy")
        self.cc.Entering_FirstName("Jessy")
        time.sleep(4)
        self.log.info("Entering Lastname-->>" + "Mande")
        self.cc.Entering_LastName("Mande")
        time.sleep(4)
        self.log.info("Entering Date OF Birth--->>" + "03-04-1996")
        self.cc.Entering_Date_Of_Birth("03/04/1996")
        time.sleep(4)
        self.log.info("Entering Address--->>" + "Wagholi, Pune")
        self.cc.Entering_Address("Wagholi Pune")
        time.sleep(4)
        self.log.info("Entering City-->>" + "Pune")
        self.cc.Entering_City("Pune")
        time.sleep(4)
        self.log.info("Entering State--->>" + "Maharashtra")
        self.cc.Entering_State("Maharashtra")
        time.sleep(4)
        self.log.info("Entering Zipcode--->>" + "444145")
        self.cc.Entering_ZipCode("444145")
        time.sleep(4)
        self.log.info("Click On Create Customer Button-->>>")
        self.cc.Click_On_CreateCustomer_Button()
        time.sleep(5)
        self.log.info("Validating Customer Creation-->>")
        if self.cc.Validate_CustomerCreated() == "Customer_Creation Pass":
            time.sleep(3)
            self.log.info("Taking Screenshot-->>")
            self.driver.save_screenshot(".\\ScreenShoot\\Test_Case_CreateNewCustomer_TC011_Is_Pass.png")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            self.log.info("Click On Logout Button--->>>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case Create New Customer TC011 In CM Is Pass\n")
            assert True

        else:
            time.sleep(3)
            self.log.info("Taking Screenshot-->>")
            self.driver.save_screenshot(".\\ScreenShoot\\Test_Case_CreateNewCustomer_TC011_Is_Fail.png")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            self.log.info("Click On Logout Button--->>>")
            self.lp.Click_On_LogOut_Button()
            time.sleep(3)
            self.log.info("Test Case Create New Customer TC011 In CM Is Fail.\n")
            assert False



