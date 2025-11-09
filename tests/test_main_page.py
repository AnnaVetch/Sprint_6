import allure
import pytest

from data import Questions
from helpers.urls import *
from pages.main_page import *

@allure.feature("Тест- переход по логотипу Скутер")
def test_click_scooter_logo_success(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_to_scooter_logo()

    assert main_page.wait_url(main_page.URL)

@allure.feature("Тест- переход по логотипу Яндекс")
def test_click_yandex_logo_success(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_to_yandex_logo()
    main_page.switch_to_new_window()

    assert main_page.wait_url(DZEN_URL)


@pytest.mark.parametrize('question_locator, answer_locator, expected_answer', [
    ((By.ID, "accordion__heading-0"), (By.ID, "accordion__panel-0"), Questions.EXPECTED_ANSWERS[0]),
    ((By.ID, "accordion__heading-1"), (By.ID, "accordion__panel-1"), Questions.EXPECTED_ANSWERS[1]),
    ((By.ID, "accordion__heading-2"), (By.ID, "accordion__panel-2"), Questions.EXPECTED_ANSWERS[2]),
    ((By.ID, "accordion__heading-3"), (By.ID, "accordion__panel-3"), Questions.EXPECTED_ANSWERS[3]),
    ((By.ID, "accordion__heading-4"), (By.ID, "accordion__panel-4"), Questions.EXPECTED_ANSWERS[4]),
    ((By.ID, "accordion__heading-5"), (By.ID, "accordion__panel-5"), Questions.EXPECTED_ANSWERS[5]),
    ((By.ID, "accordion__heading-6"), (By.ID, "accordion__panel-6"), Questions.EXPECTED_ANSWERS[6]),
    ((By.ID, "accordion__heading-7"), (By.ID, "accordion__panel-7"), Questions.EXPECTED_ANSWERS[7]),
])

@allure.feature("Проверка раздела вопросы о важном")
def test_faq(driver, question_locator, answer_locator, expected_answer):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.wait_url(main_page.URL)

    answer = main_page.get_question_answer(question_locator, answer_locator)
    assert answer == expected_answer
