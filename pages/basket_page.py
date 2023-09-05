#!/usr/bin/python3
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    #def go_to_basket_page(self):
        #self.guest_clik_button_see_basket()

    def sould_be_empty_basket(self):
        #product_name = self.browser.find_element(*BasePageLocators.BASKET_EMPTY).text
        #assert 'Ваша корзина пуста' in product_name, "Basket not emty"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRICE), "Goods in basket "

    def sould_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"
            




    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"
    
    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is not disappeared"
             
           
