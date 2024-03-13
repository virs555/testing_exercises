from functions.level_1.five_title import change_copy_item

import pytest


def test__change_copy_item__add_copy_of_if_len_is_less_than_100():
    assert change_copy_item('журнал работ') == 'Copy of журнал работ'

def test__change_copy_item__not_add_copy_of_if_len_is_greater_than_99():
    assert change_copy_item('a'*100, 100) == 'a'*100
    assert change_copy_item('a'*101, 100) == 'a'*101

def test__change_copy_item__add_copy_number_if_copy_of():
    assert change_copy_item('Copy of журнал работ', 100) == 'Copy of журнал работ (2)'

def test__change_copy_item__dont_respond_to_random_values_in_brackets_in_title():
    assert change_copy_item('Copy of журнал работ (aa)', 100) == 'Copy of журнал работ (aa) (2)'
    assert change_copy_item('Copy of журнал работ (9 9)', 100) == 'Copy of журнал работ (9 9) (2)'

def test__change_copy_item__increments_copy_val_by_1_if_copy_of():
    assert change_copy_item('Copy of журнал работ (2)', 100) == 'Copy of журнал работ (3)'

@pytest.mark.xfail(reason='если в скобках два значение увеличивает оба на единицу')
def test__change_copy_item__increments_copy_val_by_1_if_copy_of():
    assert change_copy_item('Copy of журнал работ 9 (9) (9)', 100) == 'Copy of журнал работ 9 (9) (10)'
