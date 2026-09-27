from utilities.config_reader import get_application_url


def test_open_website(driver):

    driver.get(get_application_url())

    assert "Your Store" in driver.title