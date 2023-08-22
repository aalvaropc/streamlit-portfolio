import smtplib
import ssl
import os
import environ

env = environ.Env()
environ.Env.read_env()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    USERNAME = os.environ.get('USERNAMEE')
    PASSWORD = os.environ.get('PASSWORDD')
    receiver = "aalvaropc@gmail.com"
    context  = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, receiver, message)