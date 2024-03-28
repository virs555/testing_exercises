import pytest

@pytest.fixture
def good_words():
    return ('beautiful', 'bright')
    

@pytest.fixture
def bad_words():
    return ('fucking', 'ruined')
