from functions.level_1.three_url_builder import build_url


def test__build_url__return_full_url_with_two_params():
    assert build_url('avito.ru', 'beauty', {'orderby':'asc', 'minprice':'100'}) == 'avito.ru/beauty?orderby=asc&minprice=100'

def test__build_url__return_full_url_without_params():
    assert build_url('avito.ru', 'beauty') == 'avito.ru/beauty'

def test__build_url__return_full_url_without_params_if_dict_empty():
    assert build_url('avito.ru', 'beauty', {}) == 'avito.ru/beauty'

def test__build_url__dont_return_params_delimeters_if_dict_empty():
    assert not build_url('avito.ru', 'beauty', {}) == 'avito.ru/beauty?'

def test__build_url__return_url_if_host_empty():
    assert build_url('', 'beauty', {}) == '/beauty'