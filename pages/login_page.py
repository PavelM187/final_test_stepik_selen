from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        assert "/login" in self.url, "Login is not in link presented"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.browser.find_element(*LoginPageLocators.LOGIN_MAIL)
        assert True, "Login_mail link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL)
        assert True, "Registration link is not presented"
        
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        
        
                
