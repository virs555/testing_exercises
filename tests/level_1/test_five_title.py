from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('журнал работ') == 'Copy of журнал работ'
    assert change_copy_item('a'*100, 100) == 'a'*100
    assert change_copy_item('a'*101, 100) == 'a'*101
    assert change_copy_item('Copy of журнал работ', 100) == 'Copy of журнал работ (2)'
    assert change_copy_item('Copy of журнал работ (aa)', 100) == 'Copy of журнал работ (aa) (2)'
    assert change_copy_item('Copy of журнал работ (9 9)', 100) == 'Copy of журнал работ (9 9) (2)'
    #assert change_copy_item('Copy of журнал работ 9 (9) (9)', 100) == 'Copy of журнал работ 9 (9) (10)' # не проходит, видимо я не понял суть функции или нашел баг