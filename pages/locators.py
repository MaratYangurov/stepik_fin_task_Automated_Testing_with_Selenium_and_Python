from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSW_1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSW_2 = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, '#content_inner .product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main p.price_color")
    NOTIFICATIONS = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")

class CartPageLocators:
    CONTAINER_PRODUCTS = (By.ID, "basket_formset")
    MESSAGE_BASKET_IS_EMPTY = (By.ID, "content_inner")

class BasketPageLocators:
    FORMSET = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p a')