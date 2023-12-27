import pytest
from faker import Faker
from page_object.Home_page import HomePage
from tests.BaseTest import BaseTest
from utlities import excel_utils

file_path = r"C:\\Users\\kumar\\PycharmProjects\\Selenium_python_project\\excel_sheet\\credential.xlsx"


class Test_login(BaseTest):

    @pytest.mark.parametrize("username, password", excel_utils.get_data_from_excel(file_path, "Sheet1"))
    def test_login_valid_credentials(self, username, password):
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_account_than_login()
        verify_page = login_page.login_with_credentials(username, password)
        assert verify_page.verify_login()

    def test_login_wrong_email_value(self):
        faker = Faker()
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_account_than_login()
        verify_page = login_page.login_with_credentials(faker.email(), "123456789")
        assert verify_page.error_massage_verify().__eq__("Warning: No match for E-Mail Address and/or Password.")

    def test_wrong_password(self):
        faker = Faker()
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_account_than_login()
        verify_page = login_page.login_with_credentials("abc@hotmail.com", faker.password())
        assert verify_page.error_massage_verify().__eq__("Warning: No match for E-Mail Address and/or Password.")

    def test_without_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_account_than_login()
        verify_page = login_page.login_with_credentials("", "")
        assert verify_page.error_massage_verify().__eq__("Warning: No match for E-Mail Address and/or Password.")
