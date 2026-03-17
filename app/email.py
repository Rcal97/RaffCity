#Questo script si occupa della gestione di invio email
#Invia email in modo asincrono utilizzando i threads
#fornisce la funzione send_email()
#gestisce l'invio dell'email di reset della password generando un token temporaneo per l'utente
#il server tramite il quale vengono inviate le email è configurato in config.py e nel file .flaskenv

from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread

#Invia email in un server separato utilizzando Thread
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

#Funzione generica per invio email
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    #Qui è dove si avvia un thread separato per l'invio in background
    Thread(target=send_async_email, args=(app, msg)).start()

#Funzione per il reset della password
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[RaffCity] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
