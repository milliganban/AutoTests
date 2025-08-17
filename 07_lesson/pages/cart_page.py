from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:                                                                     # Класс для работы с корзиной

    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")                             # Список товаров в корзине

    def __init__(self, driver):                                                     # Инициализация класса: принимает драйвер и создает объект WebDriverWait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):                                                             # Метод для нажатия кнопки оформления заказа
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def get_cart_items(self):                                                       # Метод для получения списка названий товаров в корзине
        items = self.wait.until(                                                    # Ожидание появления всех товаров в корзине
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )
        return [i.text for i in items]                                              # Возврат списка названий товаров
