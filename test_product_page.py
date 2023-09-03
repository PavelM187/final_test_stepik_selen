#!/usr/bin/python3
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
import pytest

xfile = 7
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
urls = [f"{product_base_link}/{no}" for no in range(10) if no != xfile]

xurl = pytest.param(product_base_link+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
urls.insert(xfile, xurl)




@pytest.mark.parametrize('link', urls)



def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_product_page()
    #time.sleep(300)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
