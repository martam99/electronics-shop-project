"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_item_price():
    item1 = Item("Смартфон", 100, 1)
    item2 = Item("Ноутбук", 1000, 3)
    item3 = Item("Кабель", 10, 5)
    item4 = Item("Мышка", 50, 5)
    item5 = Item("Клавиатура", 75, 5)
    assert item1.calculate_total_price() == 100
    assert item2.calculate_total_price() == 3000
    assert item3.calculate_total_price() == 50
    assert item4.calculate_total_price() == 250
    assert item5.calculate_total_price() == 375
    assert item1.apply_discount() == 100.0
    assert item2.apply_discount() == 1000.0
    assert item3.apply_discount() == 10.0
    assert item4.apply_discount() == 50.0
    assert item5.apply_discount() == 75.0

    Item.pay_rate = 0.4
    assert item1.apply_discount() == 40.0
    assert item2.apply_discount() == 400.0
    assert item3.apply_discount() == 4.0
    assert item4.apply_discount() == 20.0
    assert item5.apply_discount() == 30.0

    # Создаём экземпляр класса для проверки
    item6 = Item('Телефон', 10000, 5)
    # Проверяем геттер, который выводит имя товара
    assert item6.name == "Телефон"
    # Проверяем сеттер, в котором символы наименования товара не превышают 10
    with pytest.raises(Exception):
        assert item6.name == 'Iphone_x_pro'
    # Проверяем класс-метод, который создаёт экземпляр класса из файла csv
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    # Проверяем статический метод, который возвращает число из числа-строки
    assert Item.string_to_number('5.9') == 5
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('97.5') == 97

    # Проверяем магические методы `__repr__` и `__str__`
    assert repr(item1) == "Item('Смартфон', 100.0, 1)"
    assert str(item1) == "Смартфон"

    assert repr(item2) == "Item('Ноутбук', 1000, 3)"
    assert str(item2) == "Ноутбук"

    assert repr(item3) == "Item('Кабель', 10, 5)"
    assert str(item3) == "Кабель"






