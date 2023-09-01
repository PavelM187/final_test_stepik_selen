#!/usr/bin/python3
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.NAME, "registration-email")
    REGISTRATION_MAIL = (By.NAME, "registration-email")
    #REGISTRATION_PSW1 = (By.NAME, "registration-password1")
    #REGISTRATION_PSW2 = (By.NAME, "registration-password2")
    LOGIN_MAIL = (By.NAME, "login-username")
    #LOGIN_PSW = (By.NAME, "login-password")    
            
