#!/usr/bin/python3
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_BASKET).click()
        self.solve_quiz_and_get_code()



    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"
    
    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is not disappeared"
             
           
