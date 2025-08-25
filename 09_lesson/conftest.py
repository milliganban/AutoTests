import pytest
from db import SessionLocal, StudentPage

# Фикстура для подключения к БД
@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()          # создаём новую сессию
    yield session                     # отдаём её тесту
    session.close()                   # после теста закрываем соединение

# Фикстура для удобной работы со StudentPage
@pytest.fixture(scope="function")
def student_page(db_session):
    return StudentPage(db_session)    # возвращаем обёртку для работы со студентами
