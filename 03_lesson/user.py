class User:                                               # Объявляем класс с именем User
    def __init__(self, first_name, last_name):            # Определяем конструктор класса (метод, который вызывается при создании объекта)
        self.first_name = first_name                      # Сохраняем переданное имя (first_name) в атрибут self.first_name
        self.last_name = last_name                        # Сохраняем переданную фамилию (last_name) в атрибут self.last_name

    def print_first_name(self):                           # Метод для печати имени
        print(self.first_name)                            # Выводим в консоль значение атрибута first_name

    def print_last_name(self):                            # Метод для печати фамилии
        print(self.last_name)                             # Выводим в консоль значение атрибута last_name

    def print_full_name(self):                            # Метод для печати полного имени (имя + фамилия)
        print(f"{self.first_name} {self.last_name}")      # Выводим в консоль строку, состоящую из имени и фамилии через пробел