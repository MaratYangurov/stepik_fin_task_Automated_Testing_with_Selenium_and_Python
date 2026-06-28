import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestAddToCart:
    """Тесты для добавления товара в корзину"""

    @pytest.mark.parametrize(
        'link',
        [
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            pytest.param(
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                marks=pytest.mark.xfail
            ),
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
        ]
    )
    def test_guest_can_add_product_to_basket(self, browser, link):
        """
        Тест: гость может добавить товар в корзину (с решением математического alert-а)
        """
        # Открываем страницу
        browser.get(link)

        # Добавляем товар
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        button.click()

        # Решаем математический alert
        alert = browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()

        # Закрываем второй alert (если есть)
        try:
            alert = browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

        # Проверяем, что название товара совпадает с сообщением
        product_name = browser.find_element(By.CSS_SELECTOR, ".product_main h1").text
        success_message = browser.find_element(By.CSS_SELECTOR, ".alertinner strong").text

        assert product_name == success_message, f"Bug on link: {link}"


class TestProductPage:
    """Тесты для страницы товара"""

    def test_guest_should_see_login_link_on_product_page(self, browser):
        """
        Тест: гость видит ссылку на логин на странице товара
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """
        Тест: гость может перейти на страницу логина со страницы товара
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        """
        Тест: гость не видит товаров в корзине при переходе со страницы товара
        """
        # Шаг 1: Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

        # Шаг 2: Переходим в корзину из шапки
        page.go_to_basket_page()

        # Шаг 3: Проверяем, что корзина пуста
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty()

# pytest -v --tb=line --language=en test_product_page.py