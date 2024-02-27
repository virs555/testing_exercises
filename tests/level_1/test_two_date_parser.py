from functions.level_1.two_date_parser import compose_datetime_from

import datetime


def test_compose_datetime_from():
    assert compose_datetime_from("23.02.2024", "12:31") == datetime.datetime(2024, 2, 23, 12, 31)
    assert compose_datetime_from("tomorrow", "12:31") == datetime.datetime.combine(datetime.date.today(), datetime.time(12,31)) + datetime.timedelta(days=1)
