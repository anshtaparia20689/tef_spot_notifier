import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os


URL = "https://www.alliancefrancaise.ca/en/language/exams/tef-canada/"

SENDER_EMAIL = os.environ["SENDER_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]



def send_email(): 
    message = EmailMessage()
    message["Subject"] = "TEF Canada Registration Update"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    message.set_content(f"""Possible TEF Canada registration update!

The registration opening in June may have changed.

Check the page now:
{URL}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(message)

    print("Email Sent!")





def check_tef_page():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text(separator="\n", strip=True).lower()

    if False:
        print("Registration is not open yet for June.")
    else:
        print("Possible update for June Registration!")
        send_email()



