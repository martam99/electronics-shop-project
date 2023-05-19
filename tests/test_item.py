"""Здесь надо написать тесты с использованием pytest для модуля item."""
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

