import unittest
from selenium import webdriver
from utilities.config_reader import get_application_url


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_homepage_title(self):
        self.driver.get(get_application_url())

        self.assertIn("Your Store", self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()