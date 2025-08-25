def test_add_student(student_page):
    student = student_page.add_student(99999, "Beginner", "group", 1)    # Добавляем студента с ID = 99999
    fetched = student_page.get_student(99999)                            # Достаём его обратно из БД
    # Проверяем, что студент сохранился
    assert fetched is not None
    assert fetched.level == "Beginner"

    # Чистим за собой данные
    student_page.delete_student(99999)


def test_update_student(student_page):
    student_page.add_student(99998, "Elementary", "personal", 1)       # Сначала добавляем студента
    updated = student_page.update_student_level(99998, "Advanced")     # Меняем ему уровень
    assert updated.level == "Advanced"                                 # Проверяем, что обновление прошло

    # Чистим за собой данные
    student_page.delete_student(99998)


def test_delete_student(student_page):
    student_page.add_student(99997, "Pre-Intermediate", "group", 1)   # Сначала добавляем студента
    student_page.delete_student(99997)                                # Удаляем его
    deleted = student_page.get_student(99997)                         # Проверяем, что в базе его больше нет
    assert deleted is None
