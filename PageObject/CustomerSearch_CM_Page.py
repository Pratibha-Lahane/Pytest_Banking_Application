import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CustomerSearch_CM_Page:
    Text_Customer_ID_Xpath = (By.XPATH, "//input[@id='customerId']")
    Click_SearchCustomer_Button_Xpath = (By.XPATH, "//button[@type='submit']")
    Validate_CustSearch_Xpath = (By.XPATH, "//h2[normalize-space()='Edit Customer']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Entering_CustomerID(self, customer_id):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Customer_ID_Xpath))
        element = self.driver.find_element(*CustomerSearch_CM_Page.Text_Customer_ID_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.send_keys(customer_id)

    def Click_On_SearchCustomer(self):
        self.driver.find_element(*CustomerSearch_CM_Page.Click_SearchCustomer_Button_Xpath).click()

    def Validate_SearchCustomer(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Validate_CustSearch_Xpath))
        title = self.driver.find_element(*CustomerSearch_CM_Page.Validate_CustSearch_Xpath).text

        if title == "Edit Customer":
            return "Customer_Search Pass."
        else:
            return "Customer_Search Fail."






