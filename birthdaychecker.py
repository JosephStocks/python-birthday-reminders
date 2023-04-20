import datetime
import unittest
from unittest.mock import MagicMock, patch

# Replace these example birthdays with real data
birthdays = {
    "Alice": "1995-06-15",
    "Bob": "1987-04-06",
    "Carol": "2001-04-20",
    "David": "1999-05-12",
}

def get_current_date():
    return datetime.date.today()

def get_today_and_thirty_days_later():
    today = get_current_date()
    thirty_days_later = today + datetime.timedelta(days=30)
    return today, thirty_days_later

def is_birthday_today(bday_str, today):
    bday = datetime.datetime.strptime(bday_str, "%Y-%m-%d").date()
    bday_this_year = bday.replace(year=today.year)
    return bday_this_year == today

def is_birthday_in_next_30_days(bday_str, today, thirty_days_later):
    bday = datetime.datetime.strptime(bday_str, "%Y-%m-%d").date()
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

class TestBirthdayFunctions(unittest.TestCase):
    @patch('__main__.get_current_date', return_value=datetime.date(2023, 4, 6))
    def test_is_birthday_today(self, _):
        self.assertTrue(is_birthday_today("2000-04-06", get_current_date()))
        self.assertFalse(is_birthday_today("2000-04-07", get_current_date()))

    @patch('__main__.get_current_date', return_value=datetime.date(2023, 4, 6))
    def test_is_birthday_in_next_30_days(self, _):
        today, thirty_days_later = get_today_and_thirty_days_later()
        self.assertTrue(is_birthday_in_next_30_days("2000-04-20", today, thirty_days_later))
        self.assertFalse(is_birthday_in_next_30_days("2000-05-07", today, thirty_days_later))

if __name__ == "__main__":
    main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)