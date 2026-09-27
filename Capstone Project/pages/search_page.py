from selenium.webdriver.common.by import By


class SearchPage:

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(product_name)

        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_page_title(self):
        return self.driver.title