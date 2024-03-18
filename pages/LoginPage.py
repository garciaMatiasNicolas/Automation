import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from basepage import BasePage


class LoginPage(BasePage):
    __url_login_page = "https://www.saucedemo.com/v1/index.html"
    __inputs = [(By.ID, "user-name"), (By.ID, "password")]
    __submit = (By.XPATH, "//INPUT[@id='login-button']")
    __header = (By.XPATH, "//DIV[@class='app_logo']")
    __error_text = (By.XPATH, "//H3[@data-test='error']")

    def __init__(self, driver: WebDriver, username: str, password: str, is_negative: bool = False) -> object:
        self.__keys = [username, password]
        self.__is_negative = is_negative
        super().__init__(driver=driver)

    def open_url(self):
        super()._open_url(self.__url_login_page)

    def send_keys(self):
        for component, key in zip(self.__inputs, self.__keys):
            super()._type(locator=component, text=key, time=3)

    def submit_keys(self):
        super()._click(locator=self.__submit, time=3)

    def tc_login(self):
        # Make login
        self.open_url()
        self.send_keys()
        self.submit_keys()

        if self.__is_negative:
            # Verify login was unsuccessful
            try:
                text_error = super()._get_text(locator=self.__error_text, time=5)
                assert text_error == "Epic sadface: Username and password do not match any user in this service"
            except AssertionError as err:
                print(f"Error during execution of test case in login page: {str(err)}")

        else:
            # Verify login was successful
            try:
                assert super()._is_displayed(locator=self.__header)
            except AssertionError as err:
                print(f"Error during execution of test case in login page: {str(err)}")

        # Wait driver
        time.sleep(5)
