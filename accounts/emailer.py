from django.core.mail import send_mail
from django.conf import settings

def otp_email_send(email , otp):
    subject = "Your OTP Code"

    message = f"Your OTP is {otp}"

    from_email = settings.EMAIL_HOST_USER

    recipient_list = [email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )