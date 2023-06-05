from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}"

    def __add__(self, other):
        """Метод для сложения экземпляров класса по количеству товара"""
        if not isinstance(other, (Phone, Item)):
            raise Exception("Нельзя сложить атрибуты экземпляров не iPhone и Item классов")
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        """Геттер, который выводит количество SIM-карт"""
        return self.number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num: int):
        """Cеттер, в котором количество SIM-карт является целым числом больше нуля"""
        if num > 0:
            self.number_of_sim = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
