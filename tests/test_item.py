"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item1 = Item("Iphone", 1000, 25)
    item2 = Item("Fridge", 1500, 10)
    item3 = Item("TV", 2000, 5)
    assert item1.calculate_total_price() == 25000
    assert item2.calculate_total_price() == 15000
    assert item3.calculate_total_price() == 10000
    assert item1.apply_discount() == 1000.0
    assert item2.apply_discount() == 1500.0
    assert item3.apply_discount() == 2000.0

    Item.pay_rate = 0.4
    assert item1.apply_discount() == 400.0
    assert item2.apply_discount() == 600.0
    assert item3.apply_discount() == 800.0
