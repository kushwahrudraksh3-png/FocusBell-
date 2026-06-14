from twilio.rest import Client
from django.conf import settings


def send_whatsapp_message(message):
    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    msg = client.messages.create(
        from_=settings.TWILIO_WHATSAPP_FROM,
        body=message,
        to=settings.TWILIO_WHATSAPP_TO
    )

    return msg.sid