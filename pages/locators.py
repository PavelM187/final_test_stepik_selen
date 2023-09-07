#!/usr/bin/python3
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTRATION_MAIL = (By.NAME, "registration-email")
    LOGIN_MAIL = (By.NAME, "login-username")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ") 

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_SEE = (By.CSS_SELECTOR, ".btn-group :nth-child(1)")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PRICE = (By.CSS_SELECTOR, "th.total.align-right")
        
    
                   
