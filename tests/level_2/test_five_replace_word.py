from functions.level_2.five_replace_word import replace_word

def test__replace_word__replace_one_word():
    assert replace_word('шла саша по шоссе', 'саша', 'маша') == 'шла маша по шоссе'


def test__replace_word__replaced_when_lowercase():
    assert replace_word('шла саша по шоссе', 'Саша', 'маша') == 'шла маша по шоссе'

def test__replace_word__dont_replace_when_underscore():
    assert replace_word('шла_саша_по_шоссе', 'саша', 'маша') != 'шла маша по шоссе'