# python-birthday-reminders

Send sms message reminders for upcoming birthdays/events.

Command to pull fresh copy of excel file:

```bash
rclone copy googledrive:Birthdays_and_other_events.xlsx .
```

Cronjob entry:

```bash
20 7 * * * /home/jstocks/python-birthday-reminders/cron_script.sh
```
