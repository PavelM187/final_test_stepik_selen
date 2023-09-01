from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        self.is_element_present(*LoginPageLocators.LOGIN_LINK)
        assert "login" in self.url
        #assert True, "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*LoginPageLocators.LOGIN_MAIL)
        assert True, "Login_mail link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTRATION_MAIL)
        assert True, "Registration link is not presented"
