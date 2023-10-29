from datetime import date, timedelta

import pytest
from freezegun import freeze_time

from birthday_reminders.birthday_checker import (
    Birthday,
    FamilyOrFriend,
    Sex,
    SideOfFamily,
    SpecificRelation,
    build_message,
    is_birthday_in_next_30_days,
    is_birthday_today,
    is_birthday_tomorrow,
    process_birthdays,
)
from birthday_reminders.load_and_validate import RawDataEntry


# Using freeze_time to freeze the date at "2023-10-24"
@freeze_time("2023-10-24")
@pytest.mark.parametrize(
    "bday_date, expected",
    [(date(2023, 10, 24), True), (date(2023, 10, 23), False)],
)
def test_is_birthday_today(bday_date, expected):
    bday = Birthday(
        "",
        bday_date,
        True,
        Sex.m,
        FamilyOrFriend.family,
        SideOfFamily.joe,
        SpecificRelation.sibling,
    )
    assert is_birthday_today(bday, date.today()) == expected


@freeze_time("2023-10-24")
@pytest.mark.parametrize(
    "bday_date, expected",
    [(date(2023, 10, 25), True), (date(2023, 10, 24), False)],
)
def test_is_birthday_tomorrow(bday_date, expected):
    bday = Birthday(
        "",
        bday_date,
        True,
        Sex.m,
        FamilyOrFriend.family,
        SideOfFamily.joe,
        SpecificRelation.sibling,
    )
    assert is_birthday_tomorrow(bday, date.today()) == expected


@freeze_time("2023-10-15")
@pytest.mark.parametrize(
    "bday_date, expected",
    [
        (date(2023, 11, 14), True),
        (date(2023, 11, 15), False),
        (date(2024, 1, 15), False),
        (date(2023, 10, 15), False),
    ],
)
def test_is_birthday_in_next_30_days(bday_date, expected):
    bday = Birthday(
        "",
        bday_date,
        True,
        Sex.m,
        FamilyOrFriend.family,
        SideOfFamily.joe,
        SpecificRelation.sibling,
    )
    assert (
        is_birthday_in_next_30_days(
            bday, date.today(), date.today() + timedelta(days=30)
        )
        == expected
    )


def test_process_birthdays():
    raw_data = [
        RawDataEntry.model_validate(
            {
                "event_type": "birthday",
                "date": date(2023, 10, 24),
                "first_name": "John",
                "last_name": "Doe",
                "sure_about_year": "yes",
                "sex": "m",
                "family_or_friend": "family",
                "side_of_family": "joe",
                "relation": "sibling",
            }
        )
    ]
    processed = process_birthdays(raw_data)
    assert processed[0].name == "John Doe"
    assert processed[0].date == date(2023, 10, 24)
    assert processed[0].sex == Sex.m


@freeze_time("2023-10-24")
def test_build_message():
    bday = Birthday(
        "John Doe",
        date(2023, 10, 24),
        True,
        Sex.m,
        FamilyOrFriend.family,
        SideOfFamily.joe,
        SpecificRelation.sibling,
    )
    bday2 = Birthday(
        "Jane Smith",
        date(2023, 11, 10),
        True,
        Sex.f,
        FamilyOrFriend.friend,
        SideOfFamily.katie,
        SpecificRelation.friend,
    )
    message = build_message([bday, bday2])
    expected_message = (
        "Happy Birthday, John Doe!\n"
        "\nBirthdays coming up in the next 30 days:\n"
        "Jane Smith: 2023-11-10"
    )
    assert message == expected_message
