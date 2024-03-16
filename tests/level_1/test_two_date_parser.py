from functions.level_1.two_date_parser import compose_datetime_from

import datetime as dt


def test__compose_datetime_from__return_today_for_unknown_date_str():
    date_and_time = compose_datetime_from("23.02.2024", "12:31")
    assert date_and_time.date() == dt.date.today()

def test__compose_datetime_from__convert_time_from_string():
    date_and_time = compose_datetime_from("23.02.2024", "12:31")
    assert date_and_time.time() == dt.time(12, 31)

def test__compose_datetime_from__convert_24_format_time_successfully():
    date_and_time = compose_datetime_from("23.02.2024", "22:31")
    assert date_and_time.time() == dt.time(22, 31)

def test__compose_datetime_from__convert_tomorrow_date(tomorrow):
    date_and_time = compose_datetime_from("tomorrow", "12:31")
    assert date_and_time.date() == tomorrow
