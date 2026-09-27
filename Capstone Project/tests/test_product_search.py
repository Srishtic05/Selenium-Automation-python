from pages.search_page import SearchPage
from utilities.config_reader import get_application_url
from utilities.csv_reader import read_test_data


test_data = read_test_data("testdata/test_data.csv")


class TestProductSearch:

    def test_product_search(self, driver):

        driver.get(get_application_url())

        search_page = SearchPage(driver)

        search_page.search_product(
            test_data[0]["product"]
        )

        assert "Search" in driver.title