from src.item import Item


class MixinLang:
    LANG = 'EN'

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.LANG

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = 'EN'
            return self


class Keyboard(MixinLang, Item):
    def __repr__(self):
        return f"{self.name}{self.price}{self.quantity}"