import datetime
from excel_loader import load_excel_data
from send_sms import send_sms


def get_current_date():
    return datetime.date.today()


def get_today_and_thirty_days_later():
    today = get_current_date()
    thirty_days_later = today + datetime.timedelta(days=30)
    return today, thirty_days_later


def is_birthday_today(bday, today):
    bday_this_year = bday.replace(year=today.year)
    return bday_this_year == today


def is_birthday_in_next_30_days(bday, today, thirty_days_later):
    bday_this_year = bday.replace(year=today.year)
    bday_next_year = bday.replace(year=today.year + 1)

    return (today < bday_this_year <= thirty_days_later) or (
        today < bday_next_year <= thirty_days_later
    )


def main():
    # Load data from the Excel file
    data = load_excel_data("Birthdays_and_other_events.xlsx")

    # Extract the relevant fields
    birthdays = {}
    for entry in data:
        if entry["eventType"] == "Birthday" and entry["date"] is not None:
            name = f"{entry['firstName']} {entry['lastName']}"
            bday = entry["date"].date()
            birthdays[name] = bday

    today, thirty_days_later = get_today_and_thirty_days_later()

    is_birthday_today_flag = False
    upcoming_birthdays = []
    messages = []

    for name, bday_str in birthdays.items():
        if is_birthday_today(bday_str, today):
            is_birthday_today_flag = True
            messages.append(f"Happy Birthday, {name}!")

        if is_birthday_in_next_30_days(bday_str, today, thirty_days_later):
            upcoming_birthdays.append((name, bday_str))

    if not is_birthday_today_flag:
        messages.append("There are no birthdays today.")

    if upcoming_birthdays:
        messages.append("\nBirthdays coming up in the next 30 days:")
        for name, bday in sorted(upcoming_birthdays, key=lambda x: x[1]):
            messages.append(f"{name}: {bday}")
    else:
        messages.append("There are no birthdays coming up in the next 30 days.")

    send_sms("\n".join(messages))


if __name__ == "__main__":
    main()
