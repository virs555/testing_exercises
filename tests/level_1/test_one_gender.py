from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('Бежал', 'Бежала', 'male') == 'Бежал'
    assert genderalize('Бежал', 'Бежала', 'female') == 'Бежала'