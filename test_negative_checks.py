import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math



class TestNegChecks:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()

        assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        page = ProductPage(browser, link)
        page.open()

        assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_basket()

        assert page.is_disappeared(*ProductPage.SUCCESS_MESSAGE), \
            "Success message did not disappear"

# pytest -v --tb=line --language=en test_negative_checks.py