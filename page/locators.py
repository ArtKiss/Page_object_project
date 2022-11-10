from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LOGIN = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_FIELD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    PRODUCT_PAGE = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_LIST = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')


class BasketPageLocators():
    BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PROMO_CODE = (By.ID, "#voucher_form_link")
