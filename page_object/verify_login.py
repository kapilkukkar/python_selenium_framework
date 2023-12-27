from selenium.webdriver.common.by import By


class VerifyLogin:
    def __init__(self, driver):
        self.driver = driver

    verify_page_linktext = "Downloads"
    error_massage_xpath="//div[contains(text(),'Warning: No match for E-Mail Address and/or Passwo')]"

    def verify_login(self):
        return self.driver.find_element(By.LINK_TEXT, self.verify_page_linktext).is_displayed()

    def error_massage_verify(self):
        return self.driver.find_element(By.XPATH,self.error_massage_xpath).text
