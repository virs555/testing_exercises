from functions.level_4.four_lines_counter import count_lines_in


def test__count_lines_in__returns_number_of_lines(filepath):
    assert count_lines_in(filepath) == 2

def test__count_lines_in__returns_number_of_lines_ignore_string_hash_symbol(filepath):
    assert count_lines_in(filepath) == 2