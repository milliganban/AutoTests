from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
input_field.send_keys("tomsmith")
sleep(1)

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
input_field.send_keys("SuperSecretPassword!")
sleep(1)

button_login = driver.find_element(By.CSS_SELECTOR, "button.radius[type='submit']")
button_login.click()

message = driver.find_element(By.ID, "flash")
print("Текст с зелёной плашки:", message.text)
sleep(1)

driver.quit()


