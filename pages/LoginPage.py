import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from basepage import BasePage


class LoginPage(BasePage):
    __url = "https://fraudecom-nam-gestionfde-ar-desa.apps.osen02.claro.amx/"
    __inputs = [(By.ID, "username"), (By.ID, "password")]
    __submit = (By.ID, "kc-login")
    __header_title = (By.XPATH, "//H1[text()='Consulta base de riesgo']")

    def __init__(self, driver: WebDriver, username: str, password: str):
        self.__keys = [username, password]
        super().__init__(driver=driver)

    def open_risk_base(self):
        super()._open_url(self.__url)
        time.sleep(5)

    def type_username(self):
        super()._type(locator=self.__inputs[0], text=self.__keys[0], time=5)
        super()._click(locator=self.__submit, time=5)

    def type_password(self):
        super()._type(locator=self.__inputs[1], text=self.__keys[1], time=5)
        super()._click(locator=self.__submit, time=5)
        self._driver.implicitly_wait(time_to_wait=10)

    def make_login(self):
        # Make login
        self.open_risk_base()
        self.type_username()
        self.type_password()

        # Verify login was successful
        try:
            text = super()._get_text(locator=self.__header_title, time=5)
            assert text == "Consulta base de riesgo"
        except AssertionError as err:
            print(f"Error during execution of test case in login page: {str(err)}")
        time.sleep(10)





