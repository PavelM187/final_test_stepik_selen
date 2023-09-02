#!/usr/bin/python3
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #LOGIN_LINK = (By.NAME, "registration-email")
    REGISTRATION_MAIL = (By.NAME, "registration-email")
    LOGIN_MAIL = (By.NAME, "login-username")

class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")            
