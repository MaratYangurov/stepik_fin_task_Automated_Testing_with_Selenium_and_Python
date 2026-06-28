from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Страница корзины"""

    def should_be_empty(self):
        """Проверка, что корзина пуста"""
        self.should_be_empty_message()
        self.should_not_be_items()

    def should_not_be_items(self):
        """Проверка, что в корзине нет товаров (отрицательная проверка)"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"

    def should_be_empty_message(self):
        """Проверка, что есть сообщение о пустой корзине"""
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Empty basket message is not presented"

    def is_not_element_present(self, how, what, timeout=4):
        """
        Отрицательная проверка: элемент НЕ должен присутствовать на странице
        (ожидание до 4 секунд, но без ошибки, если элемент не появился)
        """
        try:
            self.browser.find_element(how, what)
            return False  # элемент найден → отрицательная проверка провалилась
        except:
            return True  # элемент не найден → отрицательная проверка пройдена

    def get_empty_basket_text(self):
        """Получение текста сообщения о пустой корзине"""
        return self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text