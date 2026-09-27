import os
import pytest
from selenium import webdriver
from utilities.config_reader import get_browser


@pytest.fixture
def driver(request):

    browser = get_browser()

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_name = f"{request.node.name}_failure.png"
        screenshot_path = os.path.join(
            "screenshots",
            screenshot_name
        )

        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)