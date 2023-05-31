import pytest

from src.phone import Phone
from src.item import Item

phone1 = Phone("HONOR X8", 150000, 25, 10)
item1 = Item("TV", 180000, 10)


def test_phone():
    assert phone1.name == "HONOR X8"
    assert phone1.price == 150000
    assert phone1.quantity == 25
    assert phone1.number_of_sim == 10
    assert repr(phone1) == "Phone('HONOR X8', 150000, 25, 10)"
    assert str(phone1) == "HONOR X8"
    assert phone1 + item1 == 35

    with pytest.raises(ValueError) as e:
        """Проверяем Cеттер, в котором количество SIM-карт является целым числом больше нуля"""
        phone1.number_of_sim = 0
        phone1.number_of_sim = -2.0
        assert str(e.value) == "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля"
        assert str(e.value) == "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля"

    with pytest.raises(Exception) as e:
        """Проверяем метод сложения экземпляров класса"""
        Phone.__add__(phone1.quantity+544)
        assert str(e.value) == "Exception: Нельзя сложить атрибуты экземпляров не iPhone и Item классов"

