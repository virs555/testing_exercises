from functions.level_1.one_gender import genderalize


def test__genderalize__return_verb_male_if_gender_male():
    assert genderalize('Бежал', 'Бежала', 'male') == 'Бежал'

def test__genderalize__return_verb_female_if_gender_female():
    assert genderalize('Бежал', 'Бежала', 'female') == 'Бежала'

def test__genderalize__return_verb_female_if_gender_unknown():
    assert genderalize('Бежал', 'Бежала', 'any_string') == 'Бежала'