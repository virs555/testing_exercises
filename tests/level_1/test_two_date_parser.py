from functions.level_1.two_date_parser import compose_datetime_from

import datetime as dt


def test__compose_datetime_from__convert_date_to_dateobj():
    date_and_time = compose_datetime_from("23.02.2024", "12:31")
    assert date_and_time.date() == dt.date.today()

def test__compose_datetime_from__convert_time_to_timeobj():
    date_and_time = compose_datetime_from("23.02.2024", "12:31")
    assert date_and_time.time() == dt.time(12, 31)

def test__compose_datetime_from__convert_24_format_time_to_timeobj():
    date_and_time = compose_datetime_from("23.02.2024", "22:31")
    assert date_and_time.time() == dt.time(22, 31)

def test__compose_datetime_from__convert_string_with_tomorrow_to_dateobj_minus_1():
    assert compose_datetime_from("tomorrow", "12:31") == dt.datetime.combine(dt.date.today(), dt.time(12,31)) + dt.timedelta(days=1)
