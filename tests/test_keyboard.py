import pytest

from src.keyboard import Keyboard

k = Keyboard('Honor', 150000, 25)


def test_keyboard():
    assert k.language == 'EN'
    assert str(k) == 'Honor'

    k.change_lang()
    assert k.language == 'RU'
    k.change_lang().change_lang()
    assert k.language == 'RU'

    with pytest.raises(AttributeError):
        k.language = 'ARM'
