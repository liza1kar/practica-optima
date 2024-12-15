import smtplib
from email.mime.text import MIMEText
import json

def send_notification(email, errors):
    with open("config.json", "r") as f:
        config = json.load(f)

    smtp_server = config["smtp_server"]
    smtp_port = config["smtp_port"]
    smtp_user = config["smtp_user"]
    smtp_password = config["smtp_password"]

    message = MIMEText("\n".join(errors))
    message['Subject'] = "System Log Errors"
    message['From'] = smtp_user
    message['To'] = email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(message)