import csv


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
        self.name = name
        self.price = price
        self.quantity = quantity

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
    def keyname(self):
        return self.name

    @keyname.setter
    def keyname(self, add_name: str):
        if len(add_name) <= 10:
            self.name = add_name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """метод, инициализирующий экземпляры класса `Item` данными из файла _src/items"""
        cls.all = []
        with open('C:/Users/User/electronics-shop-project/src/items.csv', newline='', encoding='utf-8') as csvfile:
            data = csv.DictReader(csvfile)
            for row in data:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item_1 = Item(name, price, quantity)
                cls.all.append(item_1)
            print(cls.all)

    def __repr__(self):
        return f"name={self.name}, price={self.price}, quantity={self.quantity}"

    @staticmethod
    def string_to_number(string: str):
        """Метод, возвращающий число из числа-строки"""
        num = float(string)
        int_num = int(num)
        return int_num








