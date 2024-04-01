from functions.level_4.one_brackets import delete_remove_brackets_quotes

import pytest

@pytest.mark.xfail(reason='Removes not only a curly bracket, but also the text. Probably must remove the first and last symbols.')
def test__delete_remove_brackets_quotes__remove_curly_bracket():
    assert delete_remove_brackets_quotes('{hi my name is}') == 'i my name i'

def test__delete_remove_brackets_quotes__ignore_curly_bracket_if_it_is_not_at_the_beginning():
    assert delete_remove_brackets_quotes('hi my name is}') == 'hi my name is}'