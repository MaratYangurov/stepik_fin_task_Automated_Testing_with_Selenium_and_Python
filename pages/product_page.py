from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def add_product_to_basket(self):
        button = self.browser.find_element(*self.ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        # Возвращает название товара со страницы
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        # Возвращает цену товара со страницы
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_product_name_in_message(self, expected_name):
        # Проверяем название товара в сообщении
        actual_name = self.browser.find_element(
            *self.SUCCESS_MESSAGE
        ).text
        assert actual_name == expected_name, \
            f"Expected '{expected_name}', got '{actual_name}'"

    def should_be_price_in_basket(self, expected_price):
        # Проверяем цену корзины
        actual_price = self.browser.find_element(
            *self.BASKET_PRICE
        ).text

        assert actual_price == expected_price, \
            f"Expected '{expected_price}', got '{actual_price}'"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(
            math.log(abs(12 * math.sin(float(x))))
        )
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

