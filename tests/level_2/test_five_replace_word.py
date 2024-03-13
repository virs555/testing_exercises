from functions.level_2.five_replace_word import replace_word

def test__replace_word__return_success():
    text = 'Шла саша по шоссе'
    replace_from = 'саша'
    replace_to = 'Маша'

    result = replace_word(text, replace_from, replace_to)

    assert result == 'Шла Маша по шоссе'


def test__replace_word__from_lowercase():
    text = 'Шла Саша по шоссе'
    replace_from = 'саша'
    replace_to = 'Маша'

    result = replace_word(text, replace_from, replace_to)

    assert result == 'Шла Маша по шоссе'

def test__replace_word__dont_change_underscore():
    text = 'Шла_Саша_по_шоссе'
    replace_from = 'саша'
    replace_to = 'Маша'

    result = replace_word(text, replace_from, replace_to)

    assert not result == 'Шла Маша по шоссе'