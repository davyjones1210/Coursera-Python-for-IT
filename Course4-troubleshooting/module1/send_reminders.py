#!/usr/bin/env python3

# Does not work because Zenity does not work on Windows
import datetime
import email
import smtplib
import sys
import csv

def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print(" send_reminders '<date>|<title>|<emails>' ")
    return 1


def dow(date):
    """Returns the day of the week for a given date."""
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f"Reminder: {title} on {date} ({weekday})"
    message.set_content(f"""
Hello,
This is a reminder that the meeting '{title}' is scheduled for {date} ({weekday}).
Please make sure to attend.

See you there!
""")
    return message

def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names[row[0]] = row[1]
    return names

def send_message(date, title, emails, contacts):
    """Sends the message to the specified emails."""
    smtp = smtplib.SMTP('localhost', 1025)  
    names = read_names(contacts) 
    for email in emails.split(','):
        name = names[email]
        message = message_template(date, title, name)
        message['From'] = 'nreply@example.com'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email", file=sys.stderr)
    except Exception as e:
       print("Failure to send email: {}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())

# def dow(date):
#     dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
#     return dateobj.strftime("%A")