import smtplib
from email.message import EmailMessage
import getpass

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

message_body = "Hello, My name is Bat-Ochir!"
message.set_content(message_body)

# Adding the attachments
with open('Bat.jpg', 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype="image",
                           subtype="jpg",
                           filename="Bat.jpg")

try:
    # you can use 'localhost' instead of smtp.gmail.com if on linux, because it's set automatically
    # 465 port == SSL, 587 == TSL
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # so we can see what's popping
    mail_server.set_debuglevel(1)
    # getpass is here so it won't be echoing the password
    mail_pass = getpass.getpass("Password: ")
    mail_server.login(sender, mail_pass)

    # Sending the message
    mail_server.send_message(message)

    # Exiting the smtp server
    mail_server.quit()

except:
    print('Something went wrong on your end...')

