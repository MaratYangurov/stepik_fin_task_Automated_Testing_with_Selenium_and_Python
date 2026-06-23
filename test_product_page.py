import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math



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


# pytest -v --tb=line --language=en test_product_page.py