import re
import smtplib
from email.message import EmailMessage
from pathlib import Path

log_file = Path(__file__).with_name("application.log")
log_file.touch(exist_ok=True)

logs = log_file.read_text(encoding="utf-8")

if re.search(r"\bERROR\b", logs, re.IGNORECASE):
    msg = EmailMessage()
    msg["Subject"] = "Application Error Alert"
    msg["From"] = "sender@example.com"
    msg["To"] = "selvavignesh1710@gmail.com"
    msg.set_content("ERROR keyword found in application.log")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("sender@example.com", "APP_PASSWORD")
        server.send_message(msg)

    print("Error found. Email notification sent.")
else:
    print("No errors found.")