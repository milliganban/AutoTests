from address import Address
from mailing import Mailing

to_address = Address("125075", "Москва", "Ленинградский проспект", "15", "24")
from_address = Address("190000", "Санкт-Петербург", "Невский проспект", "10", "5")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=553,
    track="RB123456789CN"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.to_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)