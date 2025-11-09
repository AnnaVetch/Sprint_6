import allure
from pages.base_page import BasePage
from locators.main_page_locators import *

class MainPage(BasePage):
    URL = BasePage.HOST

    @allure.step("Открыть главную страницу сайта ЯндексСамоката")
    def open_page(self):
        self.open(self.URL)

    @allure.step("Нажать кнопку 'Заказать' в хедере")
    def click_top_button_order(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' в футере")
    def click_bottom_button_order(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать на лого 'Самокат'")
    def click_to_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на лого 'Яндекс'")
    def click_to_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Получение ответа одной секции вопросов")
    def get_question_answer(self,question_locator,answer_locator):
        element = self.find(question_locator)
        self.scroll_to_element(element)
        self.click(question_locator)
        self.wait_for_visible(answer_locator)
        return self.get_text(answer_locator)


