import time
from selenium.webdriver.remote.webdriver import WebDriver
from pages.InventoryPage import InventoryPage
from selenium.webdriver.common.by import By


class CartPage(InventoryPage):
    __url_cart_page = "https://www.saucedemo.com/v1/cart.html"
    __products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    __prices = [29.99, 9.99]
    __label_product_A = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    __label_product_B = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    __price_selector_A = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
    __price_selector_B = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
    __buttons = {
                 "CHECKOUT": (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[2]'),
                 "CONTINUE SHOPPING": (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[1]'),
                 "REMOVE A": (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button'),
                 "REMOVE B": (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/button')
                }

    def verify_url(self):
        url_path = super().current_url

        # Verify url from actual window match cart url
        assert url_path == self.__url_cart_page

    def verify_selected_products(self):
        # Get text from labels products and save it into a list
        text_backpack = super()._get_text(locator=self.__label_product_A, time=5)
        text_bike_light = super()._get_text(locator=self.__label_product_B, time=5)
        texts = [text_backpack, text_bike_light]

        # Match texts obtained with expected texts
        for product, text in zip(self.__products, texts):
            assert product == text

    def verify_price_products(self):
        # Get text from prices products and save it into a list
        price_backpack = super()._get_text(locator=self.__price_selector_A, time=5)
        price_bike_light = super()._get_text(locator=self.__price_selector_B, time=5)
        prices_obtained = [price_backpack, price_bike_light]

        # Match prices obtained with expected prices
        for price_a, price_b in zip(self.__prices, prices_obtained):
            assert price_a == float(price_b)

    def verify_buttons_are_displayed(self):
        for button in self.__buttons.values():
            super()._is_displayed(locator=button)

    def go_to_checkout(self):
        # Add products from inventory page to the cart
        super().tc_add_products()

        # Verifications
        self.verify_selected_products()
        self.verify_price_products()
        self.verify_buttons_are_displayed()

        # If verification passed make checkout
        check_out_button = self.__buttons['CHECKOUT']
        super()._click(locator=check_out_button, time=5)

        # Wait driver
        time.sleep(5)
