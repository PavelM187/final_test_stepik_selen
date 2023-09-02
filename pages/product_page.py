#!/usr/bin/python3
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def go_to_product_page(self):
        add_basket_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        add_basket_link.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

