from selenium.webdriver.common.by import By

from page_object.error_or_register import massage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    firstname_xpath = "//input[@id='input-firstname']"
    lastname_xpath = "//input[@id='input-lastname']"
    email_xpath = "//input[@id='input-email']"
    phone_number_xpath = "//input[@id='input-telephone']"
    password_xpath = "//input[@id='input-password']"
    confirm_password_xpath = "//input[@id='input-confirm']"
    privacy_policy_xpath = "//input[@name='agree']"
    submit_button_xpath = "//input[@value='Continue']"
    first_name_error_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    last_name_error_xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_error_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    phone_number_error_xpath = "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_error_xpath = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"
    privacy_policy_error_xpath = "//div[normalize-space()='Warning: You must agree to the Privacy Policy!']"

    def enter_first_name(self, f_name):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(f_name)

    def enter_last_name(self, l_name):
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(l_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH, self.phone_number_xpath).send_keys(phone_number)

    def enter_password(self, pwd):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(pwd)

    def confirm_password(self, confirm_pwd):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_pwd)

    def select_agreement(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_xpath).click()

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
        return massage(self.driver)

    def check_first_name_assertion(self):
        return self.driver.find_element(By.XPATH, self.first_name_error_xpath).text

    def check_last_name_assertion(self):
        return self.driver.find_element(By.XPATH, self.last_name_error_xpath).text

    def check_email_assertion(self):
        return self.driver.find_element(By.XPATH, self.email_error_xpath).text

    def check_phone_number_assertion(self):
        return self.driver.find_element(By.XPATH, self.phone_number_error_xpath).text

    def check_password_assertion(self):
        return self.driver.find_element(By.XPATH, self.password_error_xpath).text

    def privacy_policy_assertion(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_error_xpath).text

    def enter_the_credentials(self, f_name, l_name, mail, phone_number, pwd, confirm_pwd, privacy_policy):
        self.enter_first_name(f_name)
        self.enter_last_name(l_name)
        self.enter_email(mail)
        self.enter_phone_number(phone_number)
        self.enter_password(pwd)
        self.confirm_password(confirm_pwd)
        if privacy_policy.__eq__("select"):
            self.select_agreement()

        return self.click_submit_button()

    def check_all_assertion(self):
        assert self.check_first_name_assertion().__eq__("First Name must be between 1 and 32 characters!")
        assert self.check_last_name_assertion().__eq__("Last Name must be between 1 and 32 characters!")
        assert self.check_email_assertion().__eq__("E-Mail Address does not appear to be valid!")
        assert self.check_phone_number_assertion().__eq__("Telephone must be between 3 and 32 characters!")
        assert self.check_password_assertion().__eq__("Password must be between 4 and 20 characters!")
        assert self.privacy_policy_assertion().__eq__("Warning: You must agree to the Privacy Policy!")
