import random
import smtplib
import traceback

from django.core.mail import send_mail
from django.conf import settings
import logging
from celery import shared_task
from smtplib import SMTPException



logger = logging.getLogger(__name__)

def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))

@shared_task
def send_otp_email(email, otp):
    """
    Send OTP to the user's email.

    Args:
        email (str): The recipient's email address.
        otp (str): The OTP to send.
    """
    subject = "Your OTP Code for Secure Login"

    message = f"""\
    Hello,

    Your One-Time Password (OTP) for logging into your account is: {otp}.

    This code is valid for a limited time. Please do not share it with anyone.

    If you did not request this OTP, please ignore this email.

    Best regards,  
    Food app Support Team  
    """

    from_email = settings.EMAIL_HOST_USER

    try:
        logger.info(f"Sending OTP to: {email}")
        send_mail(subject, message, from_email, [email],fail_silently=False)
        logger.info(f"OTP sent successfully to: {email}")
        return True #Indicate success.
    except SMTPException as e:
        # SMTPException catches many SMTP related errors, including quota exhaustion.
        logger.error(f"SMTP error sending OTP to {email}: {e}")
        if "Quota exceeded" in str(e) or "Daily sending quota exceeded" in str(e):
            raise Exception("Email sending quota exhausted. Please try again later.")
        raise e  # Raise the original error for other SMTP issues.
    except Exception as e:
        logger.error(f"Unexpected Error while sending OTP to {email}: {str(e)}")
        logger.error("Complete Traceback:\n" + traceback.format_exc())
        raise e 