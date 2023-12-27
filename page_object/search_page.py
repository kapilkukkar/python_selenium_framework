from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    displayed_element_linktext = "HP LP3065"
    verify_massage_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"

    def check_for_item(self):
        return self.driver.find_element(By.LINK_TEXT, self.displayed_element_linktext).is_displayed()

    def verify_massage(self):
        return self.driver.find_element(By.XPATH, self.verify_massage_xpath).text
