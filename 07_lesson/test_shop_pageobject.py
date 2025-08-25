import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shopping_process():                                                              # Тест для проверки процесса покупки
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))    # Инициализация драйвера Firefox

    try:
        # Авторизация
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Главная страница (товары)
        inventory = InventoryPage(driver)
        inventory.add_to_cart("add-to-cart-sauce-labs-backpack")
        inventory.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        inventory.add_to_cart("add-to-cart-sauce-labs-onesie")
        inventory.go_to_cart()

        # Корзина
        cart = CartPage(driver)
        cart_items = cart.get_cart_items()                                                # Получение списка товаров в корзине и проверка
        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        # Проверяем содержимое корзины
        assert set(cart_items) == set(expected_items), f"В корзине: {cart_items}, ожидалось: {expected_items}"

        cart.checkout()                                                                   # Переход к оформлению заказа

        # Оформление заказа 
        checkout = CheckoutPage(driver)
        checkout.fill_form("Vladimir", "Tikhonov", "123456")                              # Заполнение формы и переход к итоговой сумме
        total_value = checkout.get_total()

        # Проверка суммы
        assert total_value == "$58.29", f"Ожидалось $58.29, а получили {total_value}"

    finally:
        driver.quit()                                                                    # Закрытие драйвера
