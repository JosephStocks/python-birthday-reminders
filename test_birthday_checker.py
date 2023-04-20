import pytest
from datetime import date, timedelta
from birthday_checker import (
    get_current_date,
    get_today_and_thirty_days_later,
    is_birthday_today,
    is_birthday_in_next_30_days,
)

def test_get_today_and_thirty_days_later(mocker):
    mocker.patch("birthday_checker.get_current_date", return_value=date(2023, 4, 20))
    today, thirty_days_later = get_today_and_thirty_days_later()
    assert today == date(2023, 4, 20)
    assert thirty_days_later == date(2023, 5, 20)


@pytest.mark.parametrize(
    "bday_str, today, expected",
    [
        ("1995-06-15", date(2023, 6, 15), True),
        ("1987-04-25", date(2023, 4, 20), False),
        ("2001-04-20", date(2023, 4, 20), True),
        ("1999-05-01", date(2023, 5, 1), True),
    ],
)
def test_is_birthday_today(bday_str, today, expected):
    assert is_birthday_today(bday_str, today) == expected


@pytest.mark.parametrize(
    "bday_str, today, thirty_days_later, expected",
    [
        ("1995-06-15", date(2023, 4, 20), date(2023, 5, 20), False),
        ("1987-04-25", date(2023, 4, 20), date(2023, 5, 20), True),
        ("2001-04-20", date(2023, 4, 20), date(2023, 5, 20), False),
        ("1999-05-01", date(2023, 4, 20), date(2023, 5, 20), True),
    ],
)
def test_is_birthday_in_next_30_days(bday_str, today, thirty_days_later, expected):
    assert is_birthday_in_next_30_days(bday_str, today, thirty_days_later) == expected
