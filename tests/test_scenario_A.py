from pages.CartPage import CartPage
from pages.LoginPage import LoginPage


class TestScenarioBuyItem:

    def test_buy_item(self, driver):
        cart_page: CartPage = CartPage(driver=driver)
        cart_page.checkout()

    def test_negative_login(self, driver):
        login_page: LoginPage = LoginPage(driver=driver, username="negative", password="invalid_password",
                                          is_negative=True)
        login_page.tc_login()
