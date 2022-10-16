import requests
from datetime import datetime
from CryptocurrencyPriceTracker import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail

from .models import CryptoTracker
from .config import MAX_PRICE, MIN_PRICE, RECIPIENT


def fetch_data():

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    response = requests.request("GET", url).json()

    return float(response["bitcoin"]["usd"]) if response else None


def send_email_alert():

    subject = "welcome to GFG world"
    message = f"Hi , thank you for registering in geeksforgeeks."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        RECIPIENT,
    ]
    send_mail(subject, message, email_from, recipient_list)


def job():

    data = fetch_data()
    obj = CryptoTracker.objects.filter(latest=True).first()
    if float(data) < MIN_PRICE or float(data) > MAX_PRICE:
        send_email_alert()
    if obj:
        obj.latest = False
        obj.save()

    CryptoTracker.objects.create(name="bitcoin", price=data, latest=True).save()

    print("saved obbject")


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", seconds=30)
    scheduler.start()
