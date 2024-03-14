# --- General imports --- #
import pytest
from selenium import webdriver

# --- Chrome Driver --- #
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- Firefox Driver --- #
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# --- Chrome Options --- #
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Send 'chrome' or 'firefox' as parameter for execution"
    )


@pytest.fixture()
def driver(request):
    # Get browser given in the execution parameters
    browser = request.config.getoption("--browser")
    driver = ""
    options = Options()
    options.add_argument('--ignore-certificate-errors')

    # Instance specific Browser
    print(f"\nSetting up: {browser} driver")

    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"ERROR during execution of test: Browser {browser} not supported")

    driver.implicitly_wait(time_to_wait=10)
    yield driver

    # Tear down
    print(f"\nTear down browser: {browser} driver")
    driver.quit()