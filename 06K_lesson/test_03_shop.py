import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_process():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")       # Ввод логина
    driver.find_element(By.ID, "password").send_keys("secret_sauce")                             # Ввод пароля
    driver.find_element(By.ID, "login-button").click()
    

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()    # Добавляем рюкзак
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()                    # Добавляем футболку
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()                          # Добавляем комбинезон
    

    driver.find_element(By.ID, "shopping_cart_container").click()                                # Переход в корзину
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()
    

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Vladimir")           # Ввод имени
    driver.find_element(By.ID, "last-name").send_keys("Tikhonov")                                # Ввод фамилии
    driver.find_element(By.ID, "postal-code").send_keys("123456")                                # Ввод почтового индекса
    driver.find_element(By.ID, "continue").click()
    

    total_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))                # Ждём элемент с итоговой суммой


    total_text = total_element.text                                                              # Получаем текст
    total_value = total_text.split()[-1]                                                         # Берём последнюю часть — "$58.29"
    
    
    assert total_value == "$58.29", f"Итоговая сумма должна быть $58.29, а получилось {total_value}" # Проверяем сумму
    
    driver.quit()