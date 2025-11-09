from pages.base_page import BasePage
from locators import *
class MainPage(BasePage):
    def open_page(self):
        self.open('/')

    def start_order(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)





