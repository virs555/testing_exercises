from functions.level_4.three_promocodes import generate_promocode


def test__generate_promocode__returns_line_correct_length():
    assert len(generate_promocode(promocode_len=8)) == 8

def test__generate_promocode__returns_line_correct_length_when_i_is_too_big():
    assert len(generate_promocode(promocode_len=9999)) == 9999

def test__generate_promocode__returns_true_if_all_letters_in_the_upper_register():
    assert generate_promocode(promocode_len=8).isupper()

def test__generate_promocode__returns_false_if_letter_in_the_lower_register():
    assert generate_promocode(promocode_len=8).islower() is False