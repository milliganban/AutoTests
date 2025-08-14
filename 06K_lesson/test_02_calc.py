import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_operation():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    

    delay_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "delay")))                              # Ждём появления поля задержки
    

    delay_input.clear()                                                                  # Очищаем поле
    delay_input.send_keys("45")                                                          # Вводим задержку 45 секунд
    

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    

    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))               # Ждём появления результата 15
    

    result = driver.find_element(By.CLASS_NAME, "screen").text                           # Получаем текст с экрана
    assert result == "15", f"Ожидался результат 15, получено: {result}"                  # Проверяем, что это 15
    
    
    driver.quit()