from functions.level_1.five_title import change_copy_item

import pytest


def test__change_copy_item__copy_add_when_len_less_max():
    assert change_copy_item('журнал работ') == 'Copy of журнал работ'


@pytest.mark.parametrize(('max_leght', 'max_main_item_title_length', 'expected'), [
    ('a'*100, 100, 'a'*100),
    ('a'*101, 50, 'a'*101),
    ('a'*500, 300, 'a'*500)
])
def test__change_copy_item__dont_add_copy_when_len_greater_max(max_leght, max_main_item_title_length, expected):
    assert change_copy_item(max_leght, max_main_item_title_length) == expected

def test__change_copy_item__add_copy_number_if_copy_of_exists():
    assert change_copy_item('Copy of журнал работ', 100) == 'Copy of журнал работ (2)'

@pytest.mark.parametrize(('max_leght', 'max_main_item_title_length', 'expected'), [
    ('Copy of журнал работ (aa)', 100, 'Copy of журнал работ (aa) (2)'),
    ('Copy of журнал работ (9 9)', 100, 'Copy of журнал работ (9 9) (2)'),
])
def test__change_copy_item__dont_respond_to_other_values_in_brackets_in_title(max_leght, max_main_item_title_length, expected):
    assert change_copy_item(max_leght, max_main_item_title_length) == expected

def test__change_copy_item__increments_copy_val_by_1_if_copy_of_exists():
    assert change_copy_item('Copy of журнал работ (2)', 100) == 'Copy of журнал работ (3)'

@pytest.mark.xfail(reason='если в скобках два значения увеличивает оба на единицу')
def test__change_copy_item__increments_copy_val_by_1_if_copy_of_exists():
    assert change_copy_item('Copy of журнал работ 9 (9) (9)', 100) == 'Copy of журнал работ 9 (9) (10)'
