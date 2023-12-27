import pytest
from faker import Faker
from page_object.Home_page import HomePage
from tests.BaseTest import BaseTest


class Test_register(BaseTest):
    def test_register_with_mandatory_fields(self):
        faker = Faker()
        password = faker.password()
        home_page = HomePage(self.driver)
        register_page = home_page.click_on_account_than_register()
        massage_object = register_page.enter_the_credentials(faker.first_name(), faker.last_name(), faker.email(),
                                                             faker.phone_number(), password, password, "select")
        assert massage_object.verify_account().__eq__("Your Account Has Been Created!")

    @pytest.mark.sanity
    def test_register_with_already_email(self):
        faker = Faker()
        password = faker.password()
        home_page = HomePage(self.driver)
        register_page = home_page.click_on_account_than_register()
        massage_object = register_page.enter_the_credentials(faker.first_name(), faker.last_name(), "abc@hotmail.com",
                                                             faker.phone_number(), password, password, "select")
        assert massage_object.error_massage().__eq__("Warning: E-Mail Address is already registered!")

    @pytest.mark.regression
    def test_register_with_empty_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.click_on_account_than_register()
        register_page.enter_the_credentials("", "", "", "", "", "", "")
        register_page.check_all_assertion()
