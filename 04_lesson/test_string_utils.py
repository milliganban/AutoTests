import pytest                                                   # Импорт фреймворка
from string_utils import StringUtils                            # Импорт тестируемого класса

@pytest.fixture                                                 # Фикстура создает новый экземпляр для КАЖДОГО теста
def utils():
    """Фикстура возвращает свежий экземпляр StringUtils для каждого теста"""
    return StringUtils()                                        # Создание объекта


# Группа позитивных тестов для capitalize
@pytest.mark.positive_test                                      # Метка для группировки тестов
@pytest.mark.parametrize("input_str, expected", [               # Параметризация: один тест на несколько случаев
    ("skypro", "Skypro"),                                       # Обычная строка
    ("hello world", "Hello world"),                             # Строка с пробелом
    ("python", "Python"),                                       # Строка в нижнем регистре
    ("тест", "Тест"),                                           # Кириллица
    ("123abc", "123abc"),                                       # Числа в начале
    ("04 апреля 2023", "04 апреля 2023")                        # Комплексная строка
])
def test_capitalize_positive(utils, input_str, expected):  
    """Проверяем корректность работы capitalize с нормальными данными"""
    assert utils.capitalize(input_str) == expected              # Проверяем соответствие результата


# Группа негативных тестов для capitalize
@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                                                   # Пустая строка
    (" ", " "),                                                 # Пробел
    (None, None)                                                # None 
])
def test_test_capitalize_negative(utils, input_str, expected):
    """Тестируем граничные случаи и обработку ошибок"""
    if input_str is None:                                       # Особый случай
        with pytest.raises(AttributeError):                     
            utils.capitalize(input_str)
    
    else:
        assert utils.capitalize(input_str) == expected


# Группа позитивных тестов для trim
@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),                                    # Пространство в начале
    ("skypro", "skypro"),                                       # Без пробелов
    ("  sky pro ", "sky pro "),                                 # Пробелы внутри сохраняются
    ("   ", ""),                                                # Только пробелы
    ("04 апреля 2023", "04 апреля 2023")                        # Комплексный случай   
])
def test_trim_positive(utils, input_str, expected):
    """Проверяем базовую функциональность trim"""
    assert utils.trim(input_str) == expected


# Группа негативных тестов для trim
@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    (None, None),                                               # Передаем None 
    (123, 123),                                                 # Число вместо строки
    (["  text  "], ["  text  "]),                               # Список вместо строки
    ("", ""),                                                   # Пустая строка
    ({"key": " value "}, {"key": " value "})                    # Словарь вместо строки
])
def test_trim_negative(utils, input_str, expected):
    """Тестируем нестандартные и ошибочные входные данные"""
    if isinstance(input_str, str):                              # Если это строка - обычная проверка
        assert utils.trim(input_str) == expected
    else:                                                       # Для других типов ожидаем исключение
        with pytest.raises((AttributeError, TypeError)):
            utils.trim(input_str)


# Группа позитивных тестов для contains
@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),                                      # Символ есть
    ("SkyPro", "U", False),                                     # Символа нет
    ("Hello world", "o w", True),                               # Подстрока
    ("123", "2", True),                                         # Цифры
    ("", "", True),                                             # Пустые строки
    (" ", " ", True)                                            # Пробелы
])
def test_contains_positive(utils, string, symbol, expected):
    """Тестируем поиск символов в разных условиях"""
    assert utils.contains(string, symbol) == expected


# Группа позитивных тестов для delete_symbol
@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),                                  # Удаление одного символа
    ("SkyPro", "Pro", "Sky"),                                  # Удаление подстроки
    ("aabbcc", "b", "aacc"),                                   # Множественное удаление
    ("12345", "3", "1245"),                                    # Цифры
    ("", "a", ""),                                             # Пустая строка
    (" ", " ", "")                                             # Удаление пробела
])
def test_delete_sunbol_positive(utils, string, symbol, expected):
    """Проверяем основную функциональность удаления"""
    assert utils.delete_symbol(string, symbol) == expected