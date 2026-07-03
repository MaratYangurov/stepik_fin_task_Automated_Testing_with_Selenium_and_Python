import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestProductPage():
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    @pytest.mark.parametrize(
        'param_link',
        [
            f'{link}?promo=offer0',
            f'{link}?promo=offer1',
            f'{link}?promo=offer2',
            f'{link}?promo=offer3',
            f'{link}?promo=offer4',
            f'{link}?promo=offer5',
            f'{link}?promo=offer6',
            pytest.param(
              f'{link}?promo=offer7',
              marks=pytest.mark.xfail),
            f'{link}?promo=offer8',
            f'{link}?promo=offer9'
        ]
    )
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, param_link):
        page = ProductPage(browser, param_link)
        page.open()
        page.add_product_in_cart()
        page.solve_quiz_and_get_code()
        page.check_name_added_product_in_notification()
        page.check_price_added_product_in_notification()


    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_in_cart()
        page.should_not_be_success_message()


    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_in_cart()
        page.success_message_disappears()


    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart_page()
        cart_page = BasketPage(browser, browser.current_url)
        cart_page.should_is_basket_empty()
        cart_page.should_empty_cart_message()

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = "Qwerty123456"
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, self.link)
        page.open()

        page.add_product_in_cart()
        page.check_name_added_product_in_notification()
        page.check_price_added_product_in_notification()

# pytest -v --tb=line --language=en test_product_page.py