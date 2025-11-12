import allure
import pytest

from data import *
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Оформление заказа")
class TestOrderPage:
    @pytest.mark.parametrize('click_order_button, user_data', [
        (lambda page: page.click_top_button_order(), User1()),  # Верхняя кнопка заказа
        (lambda page: page.click_bottom_button_order(), User2())  # Нижняя кнопка заказа
    ], ids=["Заказ через верхнюю кнопку", "Заказ через нижнюю кнопку"])
    @allure.title("Тест - оформление заказа")
    def test_order_flow(self, driver, click_order_button, user_data):
        # Arrange
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Act
        main_page.open_page()
        main_page.accept_cookies()

        # вызываем переданный в параметрах метод кнопки
        click_order_button(main_page)

        order_page.fill_fields_of_client(
            user_data.name,
            user_data.surname,
            user_data.address,
            user_data.station_name,
            user_data.telephone
        )
        order_page.click_button_next()

        order_page.fill_fields_of_rent(
            user_data.date,
            user_data.color,
            user_data.comment
        )
        order_page.click_button_make_order()
        order_page.click_button_yes_confirm_order()

        # Assert
        assert order_page.get_success_message()
