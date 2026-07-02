from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def check_name_added_product_in_notification(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_H1).text
        notification_name_product = self.browser.find_element(*ProductPageLocators.NOTIFICATIONS).text
        assert name_product == notification_name_product, "в уведомлении отсутсвует наименование добавленного в корзину продукта"

    def check_price_added_product_in_notification(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        notification_price_product = self.browser.find_elements(*ProductPageLocators.NOTIFICATIONS)[2].text
        assert price_product == notification_price_product, "в уведомлении о стоимости корзины отсутсвует цена либо не верная цена продукта"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message does not disappear"


