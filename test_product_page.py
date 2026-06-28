import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from .pages.product_page import ProductPage



class TestAddToCart:
    @pytest.mark.parametrize(
        'link',
        [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                     marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
        ])
    def test_guest_can_add_product_to_basket(self, browser, link):
        browser.get(link)

        # добавляем товар
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        button.click()

        # решаем
        alert = browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()

        # второй alert с кодом
        try:
            alert = browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

        # проверки
        product_name = browser.find_element(By.CSS_SELECTOR, ".product_main h1").text
        success_message = browser.find_element(By.CSS_SELECTOR, ".alertinner strong").text

        assert product_name == success_message, f"Bug on link: {link}"

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    # test_product_page.py

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """
        Тест: гость может перейти на страницу логина со страницы товара
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

        page = ProductPage(browser, link)
        page.open()

        # Переходим на страницу логина (метод из BasePage)
        page.go_to_login_page()

        # Проверяем, что мы действительно на странице логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


# pytest -v --tb=line --language=en test_product_page.py