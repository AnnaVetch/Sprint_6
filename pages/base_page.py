import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)
        self.original_window = driver.current_window_handle

    @allure.step("Открыть страницу браузера")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти тест")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вставить текст")
    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Нажать ENTER")
    def input_enter(self,locator):
        self.input_text(locator,Keys.ENTER)

    @allure.step("Подождать появления элемента")
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться изменения URL")
    def wait_url(self, url):
        return self.wait.until(expected_conditions.url_to_be(url))
   
    @allure.step("Скроллить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 1000).until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != self.original_window:
                self.driver.switch_to.window(window)
                break
