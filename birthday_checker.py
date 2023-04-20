import datetime

# Replace these example birthdays with real data
birthdays = {
    "Alice": "1995-06-15",
    "Bob": "1987-04-25",
    "Carol": "2001-04-20",
    "David": "1999-05-01",
}


def get_current_date():
    return datetime.date.today()


def get_today_and_thirty_days_later():
    today = get_current_date()
    thirty_days_later = today + datetime.timedelta(days=30)
    return today, thirty_days_later


def is_birthday_today(bday_str, today):
    bday = datetime.date.fromisoformat(bday_str)
    bday_this_year = bday.replace(year=today.year)
    return bday_this_year == today


def is_birthday_in_next_30_days(bday_str, today, thirty_days_later):
    bday = datetime.date.fromisoformat(bday_str)
    bday_this_year = bday.replace(year=today.year)
    return today < bday_this_year <= thirty_days_later


def main():
    today, thirty_days_later = get_today_and_thirty_days_later()

    is_birthday_today_flag = False
    upcoming_birthdays = []

    for name, bday_str in birthdays.items():
        if is_birthday_today(bday_str, today):
            is_birthday_today_flag = True
            print(f"Happy Birthday, {name}!")

        if is_birthday_in_next_30_days(bday_str, today, thirty_days_later):
            upcoming_birthdays.append((name, bday_str))

    if not is_birthday_today_flag:
        print("There are no birthdays today.")

    if upcoming_birthdays:
        print("\nBirthdays coming up in the next 30 days:")
        for name, bday in sorted(upcoming_birthdays, key=lambda x: x[1]):
            print(f"{name}: {bday}")
    else:
        print("There are no birthdays coming up in the next 30 days.")


if __name__ == "__main__":
    main()
