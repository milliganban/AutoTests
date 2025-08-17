from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:                                                                            # Класс для работы со страницей оформления заказа
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):                                                                # Инициализация класса: принимает драйвер и создает объект WebDriverWait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first, last, postal):                                                  # Метод для заполнения формы оформления заказа
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)    # Ввод имени, фамилии и почтового индекса
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def get_total(self) -> str:                                                                # Метод для получения итоговой суммы заказа
        total = self.wait.until(EC.visibility_of_element_located(self.TOTAL_LABEL))            # Ожидание появления элемента с суммой и извлечение текста
        return total.text.split()[-1]                                                          # Возврат суммы
