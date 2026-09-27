# E-Commerce Web Automation — Selenium Python Framework Development
Capstone Assignment 2: Selenium Python Automation Framework Using Unittest + PyTest + Page Object Model
(OpenCart demo — https://tutorialsninja.com/demo/)

## **🎥 Project Video Demonstration**

[▶️ Watch Project Video](https://drive.google.com/file/d/1W6J6oseI_omgFrybgLYNgfFFA4xl87aO/view?usp=drive_link)




## Automated Flow

1.	Launch the browser and open the application under test.
2.	Read browser, URL, and timeout settings from a centralized configuration.
3.	Read login and product-search data from a CSV file.
4.	Log in to the e-commerce application.
5.	Verify successful login.
6.	Search for a configured product.
7.	Verify that relevant search results are displayed.
8.	Capture a screenshot automatically when a test fails.
9.	Execute tests using PyTest and include a Unittest-based test case.
10.	Generate an HTML execution report containing test results.

## Project Structure

```
selenium_python_framework/
|
|-- README.md
|-- requirements.txt
|-- pytest.ini
|-- conftest.py
|
|-- config/
|   `-- config.py
|
|-- data/
|   `-- test_data.csv
|
|-- pages/
|   |-- base_page.py
|   |-- login_page.py
|   `-- search_page.py
|
|-- utils/
|   |-- driver_factory.py
|   |-- csv_reader.py
|   |-- screenshot_utils.py
|   `-- config_reader.py
|
|-- tests/
|   |-- test_login_pytest.py
|   `-- test_search_unittest.py
|
`-- reports/
    |-- screenshots/
    `-- report.html

```

## Requirements

```
selenium
pytest
pytest-html
The exact package versions should be pinned in the final requirements.txt used for submission after the framework has been executed and verified in the target environment.

```

## How to Run the Framework

```
# 1. Create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute PyTest suite
pytest -v --html=reports/report.html --self-contained-html

# 4. Execute Unittest test
python -m unittest tests/test_search_unittest.py -v

```
Chrome is used as the default browser in the proposed configuration. Selenium 4.x can use Selenium Manager for driver resolution, avoiding the need to maintain a separate driver executable in the project.
