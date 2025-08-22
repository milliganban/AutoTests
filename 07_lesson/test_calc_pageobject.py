import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.calc_page import CalcPage


def test_calculator_operation():                                                          # Тест для проверки работы калькулятора
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))    # Инициализация драйвера Firefox

    try:
        calc = CalcPage(driver)                                                           # Создание объекта страницы калькулятора
        calc.open()                                                                       # Открытие страницы
        calc.set_delay(45)                                                                # Установка задержки вычислений (45 секунд)
        calc.click_button("7")                                                            # Нажатие кнопок
        calc.click_button("+")                                                            # Нажатие кнопок
        calc.click_button("8")                                                            # Нажатие кнопок
        calc.click_button("=")                                                            # Нажатие кнопок
        result = calc.get_result(expected="15", timeout=46)                               # Получение результата с ожиданием (таймаут 46 секунд) и проверка
        assert result == "15", f"Ожидался результат 15, получено: {result}"
    finally:
        driver.quit()                                                                     # Закрытие драйвера
