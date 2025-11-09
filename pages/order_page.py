import allure
from pages.base_page import BasePage
from locators.order_page_locators import *

class OrderPage(BasePage):
    URL = BasePage.HOST+"order"

    @allure.step("Открыть форму: Для кого самокат")
    def open_page(self):
        self.open(self.URL)

    @allure.step("Заполнить поля формы 'Для кого самокат'")
    def fill_fields_of_client(self, name, last_name, address, metro_station, phone):
        self.input_text(OrderPageLocators.INPUT_NAME, name)
        self.input_text(OrderPageLocators.INPUT_LASTNAME, last_name)
        self.input_text(OrderPageLocators.INPUT_ADDRESS, address)
        self.click(OrderPageLocators.INPUT_METRO)
        self.click(OrderPageLocators.METRO_STATION_OPTION)
        self.input_text(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step("Нажать на кнопку 'Далее'")
    def click_button_next(self):
        self.wait_for_visible(OrderPageLocators.BUTTON_NEXT)
        self.click(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить поля формы 'Про аренду'")
    def fill_fields_of_rent(self, date, color, comment):
        self.input_text(OrderPageLocators.INPUT_DATE, date)
        self.input_enter(OrderPageLocators.INPUT_DATE)
        self.click(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click(OrderPageLocators.RENTAL_PERIOD_OPTION)
        if color == "серая безысходность":
            self.click(OrderPageLocators.CHECKBOX_GREY_COLOR_SCOOTER)
        else:
            self.click(OrderPageLocators.CHECKBOX_BLACK_COLOR_SCOOTER)
        self.click(OrderPageLocators.CHECKBOX_GREY_COLOR_SCOOTER)
        self.input_text(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_button_make_order(self):
        self.wait_for_visible(OrderPageLocators.BUTTON_MAKE_ORDER)
        self.click(OrderPageLocators.BUTTON_MAKE_ORDER)

    @allure.step("Нажать на кнопку 'Да' в плейсхолдере 'Хотите оформить заказ?'")
    def click_button_yes_confirm_order(self):
        self.wait_for_visible(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)
        self.click(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)

    @allure.step("Дождаться появления плейсхолдера 'Заказ оформлен'")
    def get_success_message(self):
        return self.wait_for_visible(OrderPageLocators.SUCCESS_MESSAGE)







