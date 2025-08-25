from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:                                                                                 # Класс для работы со страницей авторизации
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):                                                                  # Инициализация класса: принимает драйвер и создает объект WebDriverWait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):                                                                              # Метод для открытия страницы авторизации
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str):                                               # Метод для авторизации
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)     # Ввод логина, пароля и нажатие кнопки входа
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
