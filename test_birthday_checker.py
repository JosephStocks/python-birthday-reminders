import datetime
import pytest
from birthday_checker import (
    get_current_date,
    get_today_and_thirty_days_later,
    is_birthday_today,
    is_birthday_in_next_30_days,
)


def test_get_current_date():
    assert isinstance(get_current_date(), datetime.date)


def test_get_today_and_thirty_days_later():
    today, thirty_days_later = get_today_and_thirty_days_later()
    assert isinstance(today, datetime.date)
    assert isinstance(thirty_days_later, datetime.date)
    assert thirty_days_later == today + datetime.timedelta(days=30)


@pytest.mark.parametrize(
    "today, bday, expected",
    [
        (datetime.date(2023, 4, 15), datetime.date(1990, 4, 15), True),
        (datetime.date(2023, 4, 16), datetime.date(1990, 4, 15), False),
    ],
)
def test_is_birthday_today(today, bday, expected):
    assert is_birthday_today(bday, today) is expected


@pytest.mark.parametrize(
    "today, thirty_days_later, bday, expected",
    [
        (
            datetime.date(2023, 4, 15),
            datetime.date(2023, 5, 15),
            datetime.date(2000, 5, 1),
            True,
        ),
        (
            datetime.date(2023, 4, 15),
            datetime.date(2023, 5, 15),
            datetime.date(2000, 7, 1),
            False,
        ),
    ],
)
def test_is_birthday_in_next_30_days(today, thirty_days_later, bday, expected):
    assert is_birthday_in_next_30_days(bday, today, thirty_days_later) is expected


@pytest.mark.parametrize(
    "today, thirty_days_later, bday, expected",
    [
        (
            datetime.date(2023, 12, 15),
            datetime.date(2024, 1, 14),
            datetime.date(2000, 1, 10),
            True,
        ),
        (
            datetime.date(2023, 12, 15),
            datetime.date(2024, 1, 14),
            datetime.date(2000, 1, 20),
            False,
        ),
    ],
)
def test_is_birthday_in_next_30_days_across_years(
    today, thirty_days_later, bday, expected
):
    assert is_birthday_in_next_30_days(bday, today, thirty_days_later) is expected
