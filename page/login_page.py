from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=5):
        super().__init__(browser, url, timeout)

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        pass_field.send_keys(password)
        rep_pass_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD)
        rep_pass_field.send_keys(password)
        registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Word login is not find in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGIN), "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION), "Registration link is not presented"
