from typing import Dict, Any                                                  # Импорт аннотаций типов
from api_client import ApiClient  


class ProjectPage:
    
    def __init__(self, client: ApiClient) -> None:
        self.client = client                                                  # Сохраняем клиент API
        self.base_path = "/api-v2/projects"                                   # Базовый путь для API проектов


    def create_project(self, payload: Dict[str, Any]):                        # Метод для создания проекта     
        return self.client.request(  
            method="POST",                                                    # HTTP-метод
            path=self.base_path,                                              # Путь к endpoint
            json=payload,                                                     # Данные проекта
        )  


    def update_project(self, project_id: str, payload: Dict[str, Any]):       # Метод для обновления проекта
        return self.client.request(  
            method="PUT",                                                     # HTTP-метод
            path=f"{self.base_path}/{project_id}",                            # Путь с ID проекта
            json=payload,                                                     # Новые данные проекта
        )


    def get_project(self, project_id: str):                                   # Метод для получения информации о проекте
        return self.client.request( 
            method="GET",                                                     # HTTP-метод
            path=f"{self.base_path}/{project_id}",                            # Путь с ID проекта
        ) 