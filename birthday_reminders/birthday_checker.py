from datetime import date, timedelta

from .load_and_validate import Birthday, load_excel_data, process_birthdays
from .load_env import get_env_var, load_env_variables
from .send_message import send_signal_message


def is_birthday_x_days_from_today(bday: Birthday, days: int) -> bool:
    x_days_from_today = date.today() + timedelta(days=days)
    return (
        bday.date.month == x_days_from_today.month
        and bday.date.day == x_days_from_today.day
    )


def is_birthday_today(bday: Birthday) -> bool:
    today = date.today()
    return bday.date.month == today.month and bday.date.day == today.day


def send_messages(birthdays: list[Birthday]) -> None:
    for birthday in birthdays:
        send_birthday_greeting(birthday)
        send_upcoming_birthday_alerts(birthday)


def send_birthday_greeting(birthday: Birthday) -> None:
    if not is_birthday_today(birthday):
        return

    message = f"Happy Birthday, {birthday.name}"
    send_signal_message(message)


def send_upcoming_birthday_alerts(birthday: Birthday) -> None:
    if not birthday.days_ahead_alert:
        return

    for days_ahead in birthday.days_ahead_alert:
        if is_birthday_x_days_from_today(birthday, days_ahead):
            date_str = birthday.date.strftime("%a, %b %d")
            message = f"BIRTHDAY IN {days_ahead} DAYS:"
            message += f" {birthday.name}'s birthday is on {date_str}"
            send_signal_message(message)


def main() -> None:
    load_env_variables()
    raw_data = load_excel_data(get_env_var("EXCEL_WORKBOOK_FILENAME"))
    birthdays = process_birthdays(raw_data=raw_data)
    send_messages(birthdays)


if __name__ == "__main__":
    main()
