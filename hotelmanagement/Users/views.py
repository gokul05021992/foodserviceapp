from django.shortcuts import render
import random
import smtplib
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from common_lib.utils import generate_otp, send_otp_email
from django.core.cache import cache  # To store OTP temporarily


# Create your views here.


@csrf_exempt
def verify_otp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        otp = data.get("otp")

        stored_otp = cache.get(email)

        if stored_otp and stored_otp == otp:
            cache.delete(email)  # Clear OTP after successful verification
            return JsonResponse({"message": "OTP verified successfully"})
        else:
            return JsonResponse({"error": "Invalid or expired OTP"}, status=400)


@csrf_exempt
def send_otp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")

        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        otp = generate_otp()
        cache.set(email, otp, timeout=300)  # Store OTP for 5 minutes

        try:
            send_otp_email(email, otp)
            return JsonResponse({"message": "OTP sent successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
