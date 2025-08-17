from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:                                                                                    # Класс для работы со страницей калькулятора

    DELAY_INPUT = (By.ID, "delay")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):                                                                                # Метод для открытия страницы калькулятора
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: int):                                                             # Метод для установки задержки вычислений (в секундах)
        delay_input = self.wait.until(EC.visibility_of_element_located(self.DELAY_INPUT))
        delay_input.clear()                                                                        # Очистка поля и ввод указанного значения
        delay_input.send_keys(str(seconds))

    def click_button(self, value: str):                                                            # Метод для нажатия кнопки калькулятора по её значению
        locator = (By.XPATH, f"//span[text()='{value}']")
        self.driver.find_element(*locator).click()

    def get_result(self, expected: str, timeout: int):                                             # Метод для получения результата вычислений
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, expected)
        )
        return self.driver.find_element(*self.RESULT_SCREEN).text
