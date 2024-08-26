from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DeleteCustomer_CM_Page:
    Click_Delete_Button_Xpath = (By.XPATH, "(//button[@type='submit'])[5]")
    Validate_Success_Msg_Xpath = (By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[9]/td[5]/form[1]/button[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Clicking_On_Delete_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Delete_Button_Xpath))
        element = self.driver.find_element(*DeleteCustomer_CM_Page.Click_Delete_Button_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Validate_Customer_Deleted(self):
        success_msg = self.driver.find_element(*DeleteCustomer_CM_Page.Validate_Success_Msg_Xpath).text
        if success_msg == "Customer deleted successfully":
            print("Test Case Is Pass")
            return "Delete_Customer Pass"
        else:
            print("Test Case Is Fail")
            return "Delete_Customer Fail"

