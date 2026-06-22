from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")

    def add_product_to_basket(self):
        button = self.browser.find_element(*self.ADD_TO_BASKET)
        button.click()

    def should_be_product_name_in_message(self):
        name = self.browser.find_element(*self.PRODUCT_NAME).text
        message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert name == message, f"Expected {name}, got {message}"

    def should_be_price_in_basket(self):
        price = self.browser.find_element(*self.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*self.BASKET_PRICE).text
        assert price == basket_price, f"Expected {price}, got {basket_price}"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

