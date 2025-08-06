from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro Max", "+7 (999) 123-45-67"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+7 (911) 765-43-21"),
    Smartphone("Xiaomi", "Redmi Note 13 Pro", "+7 (926) 345-67-89"),
    Smartphone("Google", "Pixel 9 Pro", "+7 (903) 111-22-33"),
    Smartphone("Huawei", "P60 Pro", "+7 (985) 444-55-66")
]

for smartphone in catalog:
    print(f"{smartphone.brand} | {smartphone.model} | {smartphone.phone_number}")