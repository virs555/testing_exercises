from functions.level_2.three_first import first

import pytest

def test__first__return_first_item_for_items_is_true():
    assert first([0, 1, 2], 1) == 0


def test__first__return_first_item_for_items_is_true_without_default():
    assert first([1, 2, 3]) == 1


def test__first__raise_error_for_empty_list_without_default_arg():
    with pytest.raises(AttributeError):
        first([])


def test__first__return_none_for_empty_list_and_default_argument_is_none():
    assert first([], None) == None

def test__first__return_default_for_unknown_default():
    assert first([], 123) == 123