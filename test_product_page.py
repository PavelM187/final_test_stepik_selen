#!/usr/bin/python3
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasePage
from .pages.basket_page import BasketPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
import pytest


#@pytest.mark.user_author
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "QwerTy!@$"
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = BasePage(browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        self.page.open()                      # открываем страницу
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.register_new_user(email, password)
        time.sleep(3)
        self.login_page.should_be_authorized_user()

    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/5"
        #self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        self.page = ProductPage(browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        self.page.open()                      # открываем страницу
        self.page.go_to_product_page()
        self.page.should_be_message_about_adding()
        self.page.should_be_message_basket_total()           

    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/5"
        self.page = ProductPage(browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        self.page.open()                      # открываем страницу
        self.page.should_not_be_success_message()   
         
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/5"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_product_page()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()     

    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasePage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.sould_be_empty_basket()
    basket_page.sould_be_empty_basket_message() 
    
@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/5"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_product_page()
    page.should_not_be_success_message()
    
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/5"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_not_be_success_message()
    
@pytest.mark.skip    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/5"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_product_page()
    page.should_disappeared()
    
@pytest.mark.skip 
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()     

    
    
                
