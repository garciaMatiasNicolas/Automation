import time
from pages.LoginPage import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class InventoryPage(LoginPage):
    __url_inventory_page = "https://www.saucedemo.com/v1/inventory.html"
    __btn_add_backpack = (By.XPATH, "(//BUTTON[@class='btn_primary btn_inventory'][text()='ADD TO CART'])[1]")
    __btn_add_light = (By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[3]/button')
    __submit_search = (By.XPATH, '//BUTTON[@type="submit"]')
    __toggle_cart = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    __counter_cart = (By.XPATH, '// *[ @ id = "shopping_cart_container"] / a / span')

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, username="standard_user", password="secret_sauce")

    def select_products(self):
        super()._click(locator=self.__btn_add_backpack)
        super()._click(locator=self.__btn_add_light, time=5)

    def verify_cart_counter(self):
        counter = super()._get_text(locator=self.__counter_cart, time=3)

        # Verify cart have two elements
        assert int(counter) == 2

    def navigate_to_cart(self):
        super()._click(locator=self.__toggle_cart, time=3)

    def tc_add_products(self):
        # Log in user and select products
        super().tc_login()

        # Verify current path of the window
        assert super().current_url == self.__url_inventory_page

        # Pick up products
        self.select_products()
        self.verify_cart_counter()
        self.navigate_to_cart()

        # Wait driver
        time.sleep(5)


