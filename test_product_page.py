import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from pages.product_page import ProductPage


class TestAddToCart:
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        page.should_be_product_name_in_message()
        page.should_be_price_in_basket()



# pytest -v --tb=line --language=en test_product_page.py