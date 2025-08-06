from user import User

my_user = User("Владимир", "Тихонов")    # Создаём объект (экземпляр) класса User с именем и фамилией

my_user.print_first_name()               # Вызываем метод для печати имени
my_user.print_last_name()                # Вызываем метод для печати фамилии
my_user.print_full_name()                # Вызываем метод для печати имени и фамилии