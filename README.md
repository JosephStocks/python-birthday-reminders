# python-birthday-reminders

Send sms message reminders for upcoming birthdays/events.

### Poetry configuration (THIS IS REQUIRED!)

Set the poetry configuration so that the virtual environment is created within the project

```bash
poetry config virtualenvs.in-project true
```

You can check for all config values using:

```bash
poetry config --list
```

check for current location of virtualenv using and remove it using `rm -rf`

```bash
poetry env info --path
```

then run:

```bash
poetry install
```

### Command to pull fresh copy of excel file:

```bash
rclone copy googledrive:Birthdays_and_other_events.xlsx .
```

### Cronjob entry:

```bash
25 8 * * * /bin/bash /home/jstocks/python-birthday-reminders/cron_script.sh
```

If the cronjob script doesn't work, try these below:

```bash
* * * * * /home/jstocks/.local/bin/poetry --directory /home/jstocks/python-birthday-reminders/ run python /home/jstocks/python-birthday-reminders/main.py --prod
```

OR

```bash
* * * * * /home/jstocks/.local/bin/poetry --directory /home/jstocks/python-birthday-reminders/ run python /home/jstocks/python-birthday-reminders/main.py
```
