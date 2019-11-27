from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "is not a login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert (self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_ADRESS) 
                and self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD))

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL) 
                and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD) 
                and self.is_element_present(*LoginPageLocators.REG_CONFIRM_PASSWORD))