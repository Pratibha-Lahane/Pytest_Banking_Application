from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class EditCustomer_CM_Page:
    Click_ViewAll_Customer_Xpath = (By.XPATH, "//a[normalize-space()='View All Customers']")
    Click_Edit_Button_Xpath = (By.XPATH, "//tbody/tr[7]/td[5]/a[1]")
    Text_Address_Xpath = (By.XPATH, "//input[@id='address']")
    click_SaveChanges_Xpath = (By.XPATH, "//button[normalize-space()='Save Changes']")
    Success_Msg_Xpath = (By.XPATH, "//div[@class='success-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clicking_On_View_All_Customer_List(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_ViewAll_Customer_Xpath))
        element = self.driver.find_element(*EditCustomer_CM_Page.Click_ViewAll_Customer_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Clicking_On_Edit_Button(self):
        element = self.driver.find_element(*EditCustomer_CM_Page.Click_Edit_Button_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Entering_NewAddress(self, address):
        element = self.driver.find_element(*EditCustomer_CM_Page.Text_Address_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.clear()
        element.send_keys(address)

    def Click_On_Save_Changes_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_SaveChanges_Xpath))
        element = self.driver.find_element(*EditCustomer_CM_Page.click_SaveChanges_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Validate_CustomerUpdated(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Success_Msg_Xpath))
        success_msg = self.driver.find_element(*EditCustomer_CM_Page.Success_Msg_Xpath).text
        if success_msg == "Customer updated successfully!":
            print("Test Case Is Pass")
            return "CustomerEdit_Pass"
        else:
            print("Test Case Is Fail.")
            return "CustomerEdit_Fail"

