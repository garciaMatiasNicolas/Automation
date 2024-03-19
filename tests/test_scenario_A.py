from pages.CheckoutPage import CheckOutPage
from pages.LoginPage import LoginPage


class TestScenarioBuyItem:

    def test_buy_item(self, driver):
        check_out_page_after_buy: CheckOutPage = CheckOutPage(driver=driver)
        check_out_page_after_buy.tc_complete_order()

    def test_negative_login(self, driver):
        login_page: LoginPage = LoginPage(driver=driver, username="negative", password="invalid_password",
                                          is_negative=True)
        login_page.tc_login()
