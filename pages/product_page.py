from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_cart(self):
        # Нажатие на кнопку "Добавить в корзину"
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def check_name_added_product_in_notification(self):
        # Сообщение о том, что товар добавлен в корзину.
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        notification_name_product = self.browser.find_element(*ProductPageLocators.NOTIFICATIONS).text
        assert name_product == notification_name_product, 'Отсутствует сообщение о том, что товар добавлен в корзину.'

    def check_price_added_product_in_notification(self):
        # Сообщение со стоимостью корзины.
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        notification_price_product = self.browser.find_elements(*ProductPageLocators.NOTIFICATIONS)[2].text
        assert price_product == notification_price_product, 'Отсутствует cообщение со стоимостью корзины, либо его нет.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message does not disappear"


