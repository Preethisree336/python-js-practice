

import smtplib
import ssl
smtp_server = "smtp.gmail.com"
sender_email = "preethisree336@gmail.com"
receiver_email = "biravid26@gmail.com"
password = "xgdy gcnp mmwm dptp"

message = """
Subject: Python
Successful"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
print("Email send sucessfully")

import smtplib
import ssl

server = "smtp.gmail.com"
send_email = "preethisree336@gmail.com"
receive_email = ""
password = ""
message = """
subject: hi!
preethy """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,465,)

with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
print("Email send sucessfully")
