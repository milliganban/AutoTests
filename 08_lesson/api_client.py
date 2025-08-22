import requests  
from typing import Optional, Dict, Any                                                              # Аннотации типов для лучшей читаемости кода


class ApiClient:                                                                                    # Класс для работы с API
    def __init__(self, base_url: str, token: Optional[str] = None, timeout: int = 30) -> None:      # Конструктор класса с параметрами: базовый URL, токен и таймаут
        self.base_url = base_url.rstrip("/")                                                        # Убираем завершающий слэш из базового URL для consistency
        self.session = requests.Session()                                                           # Создаем сессию для сохранения состояния (куки, заголовки) между запросами
        self.timeout = timeout                                                                      # Устанавливаем таймаут по умолчанию для всех запросов
        self.token = token                                                                          # Сохраняем токен авторизации

        self._base_headers = {                                                                      # Базовые заголовки для всех запросов
            "Accept": "application/json",                                                           # Ожидаем JSON в ответе
            "Content-Type": "application/json",                                                     # Отправляем данные в формате JSON
        } 

        if self.token:                                                                              # Если передан токен, добавляем заголовок авторизации
            self._base_headers["Authorization"] = f"Bearer {self.token}" 

    def _url(self, path: str) -> str:                                                               # Метод для формирования полного URL
        return f"{self.base_url}/{path.lstrip('/')}"                                                # Убираем лишние слэши

    def request(self, method: str, path: str, *, headers: Optional[Dict[str, str]] = None,          # Основной метод для выполнения HTTP-запросов
                params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None):

        merged_headers = dict(self._base_headers)                                                   # Копируем базовые заголовки
        if headers:                                                                                 # Если переданы дополнительные заголовки, объединяем их с базовыми
            merged_headers.update(headers) 

        response = self.session.request(                                                            # Выполняем HTTP-запрос с использованием сессии
            method=method.upper(),                                                                  # Приводим метод к верхнему регистру
            url=self._url(path),                                                                    # Формируем полный URL
            headers=merged_headers,                                                                 # Передаем объединенные заголовки
            params=params,                                                                          # Query-параметры (для GET-запросов)
            json=json,                                                                              # Тело запроса в формате JSON
            timeout=self.timeout,                                                                   # Таймаут для запроса
        )  

        return response                                                                             # Возвращаем объект ответа