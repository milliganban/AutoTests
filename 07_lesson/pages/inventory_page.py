from selenium.webdriver.common.by import By


class InventoryPage:                                         # Класс для работы со страницей товаров
    CART_BTN = (By.ID, "shopping_cart_container")            # Локатор кнопки корзины

    def __init__(self, driver):                              # Инициализация класса: принимает драйвер
        self.driver = driver

    def add_to_cart(self, item_id: str):                     # Метод для добавления товара в корзину по его ID
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):                                    # Метод для перехода в корзину
        self.driver.find_element(*self.CART_BTN).click()
