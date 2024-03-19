import time

from pages.CartPage import CartPage
from selenium.webdriver.common.by import By


class CheckOutPage(CartPage):
    __urls_checkout_page = ["https://www.saucedemo.com/v1/checkout-step-one.html",
                            "https://www.saucedemo.com/v1/checkout-step-two.html",
                            "https://www.saucedemo.com/v1/checkout-complete.html"]

    __inputs = [(By.ID, "first-name"),
                (By.ID, "last-name"),
                (By.ID, "postal-code")]

    __buttons = [(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/a'),
                 (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input'),
                 (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')]

    __total_locator = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]')

    def first_checkout(self):
        keys = ["Matias Nicolas", "Garcia", "5006"]
        # Verify we are in the first checkout page
        assert super().current_url == self.__urls_checkout_page[0]

        # Verify buttons are displayed
        for button in self.__buttons:
            super()._is_displayed(locator=button)

        # Fill the inputs
        for input_form, key in zip(self.__inputs, keys):
            super()._type(locator=input_form, text=key, time=5)

        # Navigate to second checkout
        super()._click(locator=self.__buttons[1])

    def second_checkout(self):
        # Verify current url
        assert super().current_url == self.__urls_checkout_page[1]

        # Verify prices
        tax = 3.20
        prices = [29.99, 9.99]
        total = sum(prices) + tax
        total_in_page = super()._get_text(locator=self.__total_locator, time=5)
        pivot = total_in_page.find('$')
        num = float(total_in_page[pivot + 1:])
        print(num)
        assert num == total

        # Navigate to final checkout
        super()._click(locator=self.__buttons[2], time=5)

    def tc_checkout_products(self):
        # Navigate to checkout
        super().go_to_checkout()

        # Complete form
        self.first_checkout()
        # Second checkout
        self.second_checkout()

    def tc_complete_order(self):
        # Run TC checkout products
        self.tc_checkout_products()

        # Verify url
        assert super().current_url == self.__urls_checkout_page[2]
        text_success = super()._get_text(locator=(By.XPATH, '//*[@id="checkout_complete_container"]/h2'))

        # Verify Order completion
        assert text_success == "THANK YOU FOR YOUR ORDER"





