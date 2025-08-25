from typing import Dict
import pytest
from pages.project_page import ProjectPage


# Позитивный тест: создание проекта (POST /api-v2/projects)
def test_create_project_positive(project_page: ProjectPage, unique_project_name: str):
    payload: Dict = {"title": unique_project_name}                                                               # Подготовка данных для создания проекта
    resp = project_page.create_project(payload)                                                                  # Вызов API для создания проекта
    assert resp.status_code in (200, 201), f"Unexpected status: {resp.status_code}, body: {resp.text}"           # Проверка успешного статус-кода (200 или 201)

    data = resp.json()                                                                                           # Парсинг ответа
    project_id = data.get("id")                                                                                  # Извлечение ID созданного проекта
    assert project_id, f"No 'id' in response: {data}"                                                            # Проверка, что ID присутствует в ответе

    # Делаем GET и проверяем title
    get_resp = project_page.get_project(project_id)                                                              # Получение информации о созданном проекте
    assert get_resp.status_code == 200                                                                           # Проверка успешного статус-кода
    project_data = get_resp.json()                                                                               # Парсинг ответа
    assert project_data.get("title") == unique_project_name                                                      # Проверка, что имя проекта соответствует ожидаемому


# Негативный тест: создание проекта без обязательного поля (POST /api-v2/projects)
def test_create_project_negative_missing_name(project_page: ProjectPage):
    payload: Dict = {}                                                                                     # Попытка создания проекта без обязательного поля "title"
    resp = project_page.create_project(payload)  
    assert resp.status_code in (400, 422), f"Expected 4xx, got {resp.status_code}, body: {resp.text}"      # Проверка, что сервер возвращает ошибку (400 или 422)


# Позитивный тест: чтение проекта по ID (GET /api-v2/projects/{id})
def test_get_project_positive(project_page: ProjectPage, unique_project_name: str):
    create_resp = project_page.create_project({"title": unique_project_name})                                             # Создание проекта для последующего чтения
    assert create_resp.status_code in (200, 201), f"Create failed: {create_resp.status_code}, body: {create_resp.text}"   # Проверка успешного создания

    project_id = create_resp.json().get("id")                                                                             # Извлечение ID созданного проекта
    get_resp = project_page.get_project(project_id)                                                                       # Получение информации о проекте
    assert get_resp.status_code == 200, f"Get failed: {get_resp.status_code}, body: {get_resp.text}"                      # Проверка успешного статус-кода
    assert get_resp.json().get("title") == unique_project_name, f"Name mismatch in GET: {get_resp.json()}"                # Проверка, что имя проекта соответствует ожидаемому


# Негативный тест: GET с несуществующим ID
def test_get_project_negative_wrong_id(project_page: ProjectPage):
    unknown_id = "non-existing-" + "x"*12                                                                    # Генерация несуществующего ID
    resp = project_page.get_project(unknown_id)                                                              # Попытка получения информации о несуществующем проекте
    assert resp.status_code in (400, 404), f"Expected 404/400, got {resp.status_code}, body: {resp.text}"    # Проверка, что сервер возвращает ошибку (400 или 404)


# # Позитивный тест: обновление проекта (PUT /api-v2/projects/{id})
def test_update_project_positive(project_page: ProjectPage, unique_project_name: str):
    create_resp = project_page.create_project({"title": unique_project_name})                                             # Создание проекта для последующего обновления
    assert create_resp.status_code in (200, 201), f"Create failed: {create_resp.status_code}, body: {create_resp.text}"   # Проверка успешного создания
    project_id = create_resp.json().get("id")                                                                             # Извлечение ID созданного проекта

    new_name = unique_project_name + "_updated"                                                                           # Генерация нового имени проекта
    update_resp = project_page.update_project(project_id, {"title": new_name})                                            # Обновление проекта
    assert update_resp.status_code in (200, 204), f"Update failed: {update_resp.status_code}, body: {update_resp.text}"   # Проверка успешного статус-кода (200 или 204)

    # Делаем GET и проверяем новое название
    get_resp = project_page.get_project(project_id)                                                                       # Получение обновленной информации о проекте
    assert get_resp.status_code == 200                                                                                    # Проверка успешного статус-кода
    project_data = get_resp.json()                                                                                        # Парсинг ответа
    assert project_data.get("title") == new_name                                                                          # Проверка, что имя проекта обновилось

 
# Негативный тест: обновление проекта с несуществующим ID
def test_update_project_negative_wrong_id(project_page: ProjectPage):
    unknown_id = "non-existing-" + "y"*12                                                                    # Генерация несуществующего ID
    resp = project_page.update_project(unknown_id, {"title": "whatever"})                                    # Попытка обновления несуществующего проекта
    assert resp.status_code in (400, 404), f"Expected 404/400, got {resp.status_code}, body: {resp.text}"    # Проверка, что сервер возвращает ошибку (400 или 404)