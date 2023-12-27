from selenium.webdriver.common.by import By

from page_object.Login_page import LoginPage
from page_object.register_page import RegisterPage
from page_object.search_page import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//i[@class='fa fa-search']"
    my_account_xpath = "//span[normalize-space()='My Account']"
    login_button_linktext = "Login"
    register_button_linktext = "Register"

    def search_box_element(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(product_name)

    def search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(By.LINK_TEXT, self.login_button_linktext).click()

    def click_on_register(self):
        self.driver.find_element(By.LINK_TEXT, self.register_button_linktext).click()

    def search_for_product(self, product):
        self.search_box_element(product)
        self.search_button()
        return SearchPage(self.driver)

    def click_on_account_than_login(self):
        self.click_on_my_account()
        self.click_on_login_button()
        return LoginPage(self.driver)

    def click_on_account_than_register(self):
        self.click_on_my_account()
        self.click_on_register()
        return RegisterPage(self.driver)
