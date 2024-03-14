from pages.LoginPage import LoginPage
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ConsultPage(LoginPage):
    __select_reason = (By.ID, "search_reason")
    __opt_case = ()
    __submit_search = (By.XPATH, "//BUTTON[@type='submit']")

    def __init__(self, case_type: str, opt_reason: str, driver: WebDriver):
        super().__init__(driver, username="EXB24140", password="Gordalove12*")
        self.__opt_reason = opt_reason

        if case_type == 'open':
            self.__opt_case = (By.XPATH, "(//INPUT[@type='radio'])[4]")
        elif case_type == 'close':
            self.__opt_case = (By.XPATH, "(//INPUT[@type='radio'])[5]")
        else:
            raise ValueError("Opt case not match")

    def select_reason(self):
        super().make_login()
        super()._select_text(locator=self.__select_reason, option=self.__opt_reason, time=15)

    def select_opt_case(self):
        super()._click(locator=self.__opt_case, time=3)

    def search_risk_data(self):
        super()._click(locator=self.__opt_case, time=3)
        time.sleep(3)
