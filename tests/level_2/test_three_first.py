from functions.level_2.three_first import first

import pytest

def test__first__list_ints():
    items = [0, 1, 2]
    default = 1

    result = first(items, default)

    assert result == 0


def test__first__without_default():
    items = [1, 2, 3]

    result = first(items)

    assert result == 1


def test__first__list_empty_without_default(): #Тут есть сомнения по оформлению
    items = []

    with pytest.raises(AttributeError):
        first(items)


def test__first__list_empty_default_none():
    items = []
    default = None

    result = first(items, default)

    assert result == None

def test__first__list_empty_default_int():
    items = []
    default = 123

    result = first(items, default)

    assert result == 123