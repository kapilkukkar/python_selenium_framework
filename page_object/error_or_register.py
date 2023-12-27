from selenium.webdriver.common.by import By


class massage:
    def __init__(self, driver):
        self.driver = driver

    verify_account_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"
    error_massage_xpath = "//div[normalize-space()='Warning: E-Mail Address is already registered!']"

    def verify_account(self):
        return self.driver.find_element(By.XPATH, self.verify_account_xpath).text

    def error_massage(self):
        return self.driver.find_element(By.XPATH,self.error_massage_xpath).text
