from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверяет, что в URL присутствует подстрока "login"
        current_url = self.browser.current_url
        assert "login" in current_url, f'Expected substring "login" in URL, but received "{current_url}"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), 'Login form is not presented on the page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), 'Register form is not presented on the page'