# Загружаем переменные окружения из файла .env
from dotenv import load_dotenv
load_dotenv()
# Импорт необходимых библиотек
import os                                                           # Для работы с переменными окружения
import uuid                                                         # Для генерации уникальных идентификаторов

import pytest  
# Импорт моих классов
from api_client import ApiClient  
from pages.project_page import ProjectPage  



@pytest.fixture(scope="session")                                    # Фикстура для получения базового URL из переменных окружения
def base_url() -> str:
    return os.getenv("YOUGILE_BASE_URL", "https://yougile.com")     # Значение по умолчанию


@pytest.fixture(scope="session")                                    # Фикстура для получения токена авторизации из переменных окружения
def token() -> str:
    return os.getenv("YOUGILE_TOKEN", "")                           # Пустая строка по умолчанию


@pytest.fixture(scope="session")                                    # Фикстура для создания экземпляра API-клиента
def api_client(base_url: str, token: str) -> ApiClient:
    return ApiClient(base_url=base_url, token=token)                # Передаем базовый URL и токен


@pytest.fixture(scope="session")                                    # Фикстура для создания экземпляра страницы проекта
def project_page(api_client: ApiClient) -> ProjectPage:
    return ProjectPage(client=api_client)                           # Инициализируем клиентом API


@pytest.fixture()                                                   # Фикстура для генерации уникального имени проекта
def unique_project_name() -> str:
    return f"hw_lesson8_project_{uuid.uuid4().hex[:8]}"             # Уникальное имя с префиксом


def pytest_collection_modifyitems(config, items):                   # Хук для модификации тестов при коллекции
    has_token = bool(os.getenv("YOUGILE_TOKEN"))                    # Проверяем, установлен ли токен в окружении
    if has_token:  
        return                                                      # Если токен есть, ничего не меняем
    for item in items:                                              # Если токена нет, помечаем все тесты как ожидаемые к провалу
        item.add_marker(pytest.mark.xfail(reason="Не задан YOUGILE_TOKEN в окружении", run=False)) 