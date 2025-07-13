import smtplib

# mail_server = smtplib.SMTP('localhost')
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)

import getpass

mail_pass = getpass.getpass('Password? ')
print(mail_pass)
mail_server.login(sender, mail_pass)