from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CreateCustomer_CM_Page:
    Click_CustomerManagement_Xpath = (By.XPATH, "//a[normalize-space()='Customer Management']")
    Click_CreateNewCustomer_Xpath = (By.XPATH, "//a[normalize-space()='Create Customer']")
    Text_UserId_Xpath = (By.XPATH, "//input[@id='userId']")
    Text_FirstName_Xpath = (By.XPATH, "//input[@id='firstName']")
    Text_LastName_Xpath = (By.XPATH, "//input[@id='lastName']")
    Text_Date_of_Birth_Xpath = (By.XPATH, "//input[@id='dateOfBirth']")
    Text_Address_Xpath = (By.XPATH, "//input[@id='address']")
    Text_City_Xpath = (By.XPATH, "//input[@id='city']")
    Test_State_Xpath = (By.XPATH, "//input[@id='state']")
    Text_Zip_Code_Xpath = (By.XPATH, "//input[@id='zipCode']")
    Click_On_CreateCustomer_Button_Xpath = (By.XPATH, "//button[@type='submit']")
    Success_Msg_Xpath = (By.XPATH, "//div[@class='success-message']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_On_CustomerManagement_Tab(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_CustomerManagement_Xpath))
        element = self.driver.find_element(*CreateCustomer_CM_Page.Click_CustomerManagement_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.click()

    def Click_CreateCustomer(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_CreateNewCustomer_Xpath))
        element = self.driver.find_element(*CreateCustomer_CM_Page.Click_CreateNewCustomer_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Entering_UserId(self, userid):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_UserId_Xpath))
        self.driver.find_element(*CreateCustomer_CM_Page.Text_UserId_Xpath).send_keys(userid)

    def Entering_FirstName(self, firstname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_FirstName_Xpath))
        element = self.driver.find_element(*CreateCustomer_CM_Page.Text_FirstName_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(firstname)

    def Entering_LastName(self, lastname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_LastName_Xpath))
        self.driver.find_element(*CreateCustomer_CM_Page.Text_LastName_Xpath).send_keys(lastname)

    def Entering_Date_Of_Birth(self, dob):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Date_of_Birth_Xpath))
        element = self.driver.find_element(*CreateCustomer_CM_Page.Text_Date_of_Birth_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(dob)

    def Entering_Address(self, address):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Address_Xpath))
        element = self.driver.find_element(*CreateCustomer_CM_Page.Text_Address_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(address)

    def Entering_City(self, city):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_City_Xpath))
        element = self.driver.find_element(*CreateCustomer_CM_Page.Text_City_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(city)

    def Entering_State(self, state):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Test_State_Xpath))
        self.driver.find_element(*CreateCustomer_CM_Page.Test_State_Xpath).send_keys(state)

    def Entering_ZipCode(self, zipcode):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Zip_Code_Xpath))
        self.driver.find_element(*CreateCustomer_CM_Page.Text_Zip_Code_Xpath).send_keys(zipcode)

    def Click_On_CreateCustomer_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_On_CreateCustomer_Button_Xpath))
        self.driver.find_element(*CreateCustomer_CM_Page.Click_On_CreateCustomer_Button_Xpath).click()

    def Validate_CustomerCreated(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Success_Msg_Xpath))
        success_msg = self.driver.find_element(*CreateCustomer_CM_Page.Success_Msg_Xpath).text
        print(success_msg)
        if success_msg == "Customer created successfully":
            print("Test Case Create Customer CM Is Successfully Pass..")
            return "Customer_Creation Pass"

        else:
            print("Test Case Create Customer CM Is Fail..")
            return "Customer_Creation Fail"

