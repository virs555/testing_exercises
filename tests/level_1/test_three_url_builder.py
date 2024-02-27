from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('avito.ru', 'beauty', {'orderby':'asc', 'minprice':'100'}) == 'avito.ru/beauty?orderby=asc&minprice=100'
    assert build_url('avito.ru', 'beauty') == 'avito.ru/beauty'
