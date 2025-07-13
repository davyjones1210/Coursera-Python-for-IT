from email.message import EmailMessage
message = EmailMessage()
# print(message)

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
# print(message)

# From: me@example.com
# To: you@example.com

message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
# print(message)

# From: me@example.com
# To: you@example.com
# Subject: Greetings from me@example.com to you@example.com!

body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)

# print(message)

import os.path
attachment_path = "hopper.jpeg"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
# print(mime_type)


mime_type, mime_subtype = mime_type.split('/', 1)
# print(mime_type)

print(mime_subtype)

with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
 
# print(message)


import smtplib

# mail_server = smtplib.SMTP('localhost')
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)

import getpass

mail_pass = getpass.getpass('Password? ')
print(mail_pass)
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()