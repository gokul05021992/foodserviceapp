import random
import smtplib
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    """
    Send OTP to the user's email.

    Args:
        email (str): The recipient's email address.
        otp (str): The OTP to send.
    """
    subject = "Your OTP for Login"
    message = f"Your OTP for login is: {otp}. Please do not share it with anyone."
    from_email = settings.EMAIL_HOST_USER

    try:
        logger.info(f"Sending OTP to: {email}")
        send_mail(subject, message, from_email, [email])
        logger.info(f"OTP sent successfully to: {email}")
        return True #Indicate success.
    except Exception as e:
        logger.error(f"Error sending OTP to {email}: {e}")
        return False #Indicate failure.