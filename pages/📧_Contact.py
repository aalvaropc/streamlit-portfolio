import streamlit as st
import re
from send_email import send_email

def display():
    st.header("Contacto")
    with st.form(key="email_form"):
        name = st.text_input("Ingresa tu nombre completo")
        user_email = st.text_input("Ingresa tu e-mail")
        raw_message = st.text_area("Ingresa tu mensaje")
        message = f"""\
Subject: Nuevo email de {name}

From: {user_email}
{raw_message}
"""
        button = st.form_submit_button("Enviar")
        if button:
            if validate(name, user_email, raw_message): 
                send_email(message)
                st.info("Mensaje enviado")

def validate(nombre, email, mensaje):
    if not nombre or not mensaje or not email:
        st.warning("Por favor complete las entradas")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.warning("Por favor ingrese un e-mail válido")
    else:
        return True
    return False

display()