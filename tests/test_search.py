import pytest
from page_object.Home_page import HomePage
from tests.BaseTest import BaseTest


class Test_search(BaseTest):
    def test_search_for_a_validation(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("HP")
        assert search_page.check_for_item()

    def test_search_for_negative_data(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("Honda")
        assert search_page.verify_massage().__contains__("There is no product that matches the search criteria.")

    @pytest.mark.sanity
    def test_search_for_empty_data(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("")
        assert search_page.verify_massage().__contains__("There is no product that matches the search criteria.")
