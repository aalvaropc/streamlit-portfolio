import smtplib
import ssl
import os
# import environ
import streamlit as st

# env = environ.Env()
# environ.Env.read_env()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    USERNAME = st.secrets["USERNAMEE"]
    PASSWORD = st.secrets["PASSWORDD"]
    receiver = "aalvaropc@gmail.com"
    context  = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, receiver, message)