from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.FORMSET),\
            'The cart should be empty, but it contains an item.'

    def should_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
            '"Empty cart" message is missing.'