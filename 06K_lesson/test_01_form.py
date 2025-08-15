from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_form_submission():
    driver_path = r"C:\Users\Vladimir\Desktop\Edgedriver\msedgedriver.exe"                  # Путь к драйверу Edge (указан вручную из-за сложностей с системным прокси)
    driver = webdriver.Edge(service=EdgeService(driver_path))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='first-name']")))         # Ждём появления поля "First name"
    

    driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")                  # Оставляем поле "Zip code" пустым
    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    

    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-outline-primary")))               # Ждём, пока кнопка "Submit" станет кликабельной
    submit_btn.click()
    

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger")))         # Ждём, пока zip-code подсветится красным
    

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class"), "Zip code должен быть подсвечен красным"    # Проверяем, что оно красное
    

    valid_fields = [                                                                         # Список всех остальных полей, которые должны быть зелёными
        "first-name", "last-name", "address", "city", "country",
        "e-mail", "phone", "job-position", "company"
    ]
    

    for field_id in valid_fields:                                                            # Перебираем список
        field = driver.find_element(By.ID, field_id)                                         # Находим поле
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} должно быть зелёным" # Проверяем, что оно зелёное
    
    
    driver.quit()