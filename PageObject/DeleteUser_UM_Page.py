from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DeleteUserUM_Page:
    Click_Page_Num_Css = (By.CSS_SELECTOR, "a[href='?page=5']")
    CLick_ON_Delete_Xpath = (By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[10]/td[4]/form[1]/button[1]")
    validate_DeleteUser_Xpath = (By.XPATH, "//div[@class='error-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_Page_Number(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Page_Num_Css))
        element = self.driver.find_element(*DeleteUserUM_Page.Click_Page_Num_Css)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Click_On_DeleteUser(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.CLick_ON_Delete_Xpath))
        element = self.driver.find_element(*DeleteUserUM_Page.CLick_ON_Delete_Xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        element.click()

    def Validate_DeleteUser(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.validate_DeleteUser_Xpath))
        error_msg = (self.driver.find_element(*DeleteUserUM_Page.validate_DeleteUser_Xpath)).text
        print(error_msg)
        if error_msg == "User not found":
            print("Test Case UM Delete User Is Pass")
            return "User_Deleted Pass"
        else:
            print("Test Case UM Delete User Is Failed.")
            return "User_Deleted Fail"
