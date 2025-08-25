# Импортируем необходимые модули из SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/QA"

Base = declarative_base()                                        # Создаём "базовый класс" для моделей (таблиц)
engine = create_engine(DATABASE_URL)                             # Создаём движок (engine) — это объект, который знает, как подключаться к БД
SessionLocal = sessionmaker(bind=engine)                         # Создаём фабрику сессий — каждый раз, когда мы вызываем SessionLocal(), получаем объект для работы с БД

# Определяем модель (таблицу) "subject"
class Subject(Base):
    __tablename__ = "subject"                                    # имя таблицы в БД

    subject_id = Column(Integer, primary_key=True)               # первичный ключ
    subject_title = Column(String, nullable=False)               # название предмета (обязательное поле)

# Определяем модель (таблицу) "student"
class Student(Base):
    __tablename__ = "student"                                    # имя таблицы в БД

    user_id = Column(Integer, primary_key=True)                     # идентификатор студента (ключ)
    level = Column(String)                                          # уровень студента
    education_form = Column(String)                                 # форма обучения
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))  # внешний ключ → ссылка на таблицу subject

    def __repr__(self):
        return f"<Student user_id={self.user_id}, level={self.level}, form={self.education_form}>"

# PageObject для студентов
class StudentPage:
    def __init__(self, db_session):
        self.db = db_session                                         # получаем объект сессии для работы с БД

# Метод для добавления студента
    def add_student(self, user_id, level, education_form, subject_id):
        student = Student(user_id=user_id, level=level, education_form=education_form, subject_id=subject_id)
        self.db.add(student)                                         # добавляем студента в сессию
        self.db.commit()                                             # фиксируем изменения в БД (INSERT)
        return student

# Метод для получения студента по user_id
    def get_student(self, user_id):
        return self.db.query(Student).filter_by(user_id=user_id).first()

# Метод для обновления уровня студента
    def update_student_level(self, user_id, new_level):
        student = self.get_student(user_id)                        # находим студента
        if student:
            student.level = new_level                              # меняем поле level
            self.db.commit()                                       # сохраняем изменения (UPDATE)
        return student

# Метод для удаления студента
    def delete_student(self, user_id):
        student = self.get_student(user_id)                         # находим студента
        if student:
            self.db.delete(student)                                 # удаляем объект
            self.db.commit()                                        # фиксируем изменения (DELETE)
        return student
