import csv
import os.path
from pprint import pprint


class InstantiateCSVError(Exception):
    """Класс-исключение, в случае повреждения файла"""

    def __init__(self):
        self.file_msg = "_Файл поврежден_"

    def __str__(self):
        return self.file_msg


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity}"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * Item.pay_rate

    @property
    def name(self):
        """Геттер, который выводит имя товара"""
        return self.__name

    @name.setter
    def name(self, add_name: str):
        """Cеттер, в котором символы наименования товара не превышают 10"""
        if len(add_name) <= 10:
            self.__name = add_name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        """метод, инициализирующий экземпляры класса `Item` данными из файла _src/items"""
        cls.all = []
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    elements = (row['name'], row['price'], row['quantity'])
                    cls.all.append(elements)
                return cls.all

        except KeyError:
            raise InstantiateCSVError

        except FileNotFoundError:
            raise FileNotFoundError



    @staticmethod
    def string_to_number(string: str):
        """Метод, возвращающий число из числа-строки"""
        num = float(string)
        int_num = int(num)
        return int_num


# print(Item.instantiate_from_csv('C:/Users/User/electronics-shop-project/src/item.csv'))
# print()
