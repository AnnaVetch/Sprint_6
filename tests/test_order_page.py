import allure
import pytest

from data import *
from pages import main_page
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.mark.parametrize('order_button, user_data', [
    ('top', User1()),  # Верхняя кнопка заказа с данными первого пользователя
    ('bottom', User2())  # Нижняя кнопка заказа с данными второго пользователя
])

@allure.feature("Тест - оформление заказа")
def test_order_flow(driver, order_button, user_data):
    # Arrange
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    # Act
    main_page.open_page()
    main_page.accept_cookies()

    if order_button == 'top':
        main_page.click_top_button_order()
    else:
        main_page.click_bottom_button_order()

    order_page.fill_fields_of_client(
        user_data.name,
        user_data.surname,
        user_data.address,
        user_data.station_name,
        user_data.telephone)
    order_page.click_button_next()

    order_page.fill_fields_of_rent(
        user_data.date,
        user_data.color,
        user_data.comment)
    order_page.click_button_make_order()
    order_page.click_button_yes_confirm_order()

    # Assert
    assert order_page.get_success_message()
