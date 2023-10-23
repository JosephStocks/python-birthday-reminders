from dataclasses import dataclass
from datetime import date, timedelta
from enum import StrEnum, auto
from typing import Tuple

from .excel_loader import RawDataEntry, load_excel_data
from .send_message import send_signal_message


class FamilyOrFriend(StrEnum):
    family = auto()
    friend = auto()


class SpecificRelation(StrEnum):
    spouse = auto()
    child = auto()
    sibling = auto()
    parent = auto()
    grandparent = auto()
    sibling_in_law = auto()
    niece_or_nephew = auto()
    friend = auto()


class Sex(StrEnum):
    m = auto()
    f = auto()


class SideOfFamily(StrEnum):
    joe = auto()
    katie = auto()
    both = auto()


@dataclass
class Birthday:
    name: str
    date: date
    sure_about_year: bool
    sex: Sex
    family_or_friend: FamilyOrFriend
    side_of_family: SideOfFamily
    relation: SpecificRelation


def get_today_and_thirty_days_later() -> Tuple[date, date]:
    thirty_days_later = date.today() + timedelta(days=30)
    return date.today(), thirty_days_later


def is_birthday_today(bday: Birthday, today: date) -> bool:
    return bday.date.month == today.month and bday.date.day == today.day


def is_birthday_tomorrow(bday: Birthday, today: date) -> bool:
    bday_this_year = bday.date.replace(year=today.year)
    bday_next_year = bday.date.replace(year=today.year + 1)
    tomorrow = today + timedelta(days=1)
    return bday_this_year == tomorrow or bday_next_year == tomorrow


def is_birthday_in_next_30_days(
    bday: Birthday, today: date, thirty_days_later: date
) -> bool:
    bday_this_year = bday.date.replace(year=today.year)
    bday_next_year = bday.date.replace(year=today.year + 1)

    return (today < bday_this_year <= thirty_days_later) or (
        today < bday_next_year <= thirty_days_later
    )


def process_birthdays(raw_data: list[RawDataEntry]) -> list[Birthday]:
    birthdays: list[Birthday] = []
    for entry in raw_data:
        if entry.event_type == "birthday" and entry.date is not None:
            name = f"{entry.first_name} {entry.last_name}".strip()
            date = entry.date.date()
            sure_about_year = entry.sure_about_year == "yes"
            sex = Sex[entry.sex]
            family_or_friend = FamilyOrFriend[entry.family_or_friend]
            side_of_family = SideOfFamily[entry.side_of_family]
            relation = SpecificRelation[entry.relation]

            birthday = Birthday(
                name,
                date,
                sure_about_year,
                sex,
                family_or_friend,
                side_of_family,
                relation,
            )
            birthdays.append(birthday)
    return birthdays


def build_message(birthdays: list[Birthday]) -> str:
    today, thirty_days_later = get_today_and_thirty_days_later()

    is_birthday_today_flag = False
    upcoming_birthdays: list[Tuple[str, date]] = []
    messages: list[str] = []

    for birthday in birthdays:
        if is_birthday_today(birthday, today):
            is_birthday_today_flag = True
            messages.append(f"Happy Birthday, {birthday.name}!")

        if is_birthday_in_next_30_days(birthday, today, thirty_days_later):
            upcoming_birthdays.append((birthday.name, birthday.date))

    if not is_birthday_today_flag:
        messages.append("There are no birthdays today.")

    if upcoming_birthdays:
        messages.append("\nBirthdays coming up in the next 30 days:")
        for name, bday in sorted(
            upcoming_birthdays, key=lambda x: (x[1].month, x[1].day)
        ):
            messages.append(f"{name}: {bday}")
    else:
        messages.append("There are no birthdays coming up in the next 30 days.")

    return "\n".join(messages)


def main() -> None:
    raw_data = load_excel_data("Birthdays_and_other_events.xlsx")
    birthdays = process_birthdays(raw_data)
    full_message = build_message(birthdays)
    send_signal_message(full_message)


if __name__ == "__main__":
    main()
