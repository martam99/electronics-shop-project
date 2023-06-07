from src.item import Item


class MixinLang:
    LANG = 'EN'

    def __init__(self):
        self.__language = self.LANG

    @property
    def language(self):
        return self.LANG

    def change_lang(self):
        if self.LANG == "EN":
            self.LANG = "RU"
            return self
        else:
            self.LANG = 'EN'
            return self


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

