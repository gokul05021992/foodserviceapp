from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework.authtoken.models import Token
import datetime
from common_lib.utils import generate_otp, send_otp_email
from django.core.cache import cache  # To store OTP temporarily  
from django.contrib.auth.models import User  
from django.contrib.auth import login  # Import login function
from django.contrib.sessions.models import Session  # Import session model
from django.contrib.auth import get_user_model
import time

User = get_user_model()

@csrf_exempt
def verify_otp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        otp = data.get("otp")

        stored_otp = cache.get(email)

        if stored_otp and stored_otp == otp:
            cache.delete(email)  # Clear OTP after successful verification

            # Get or create user
            user, created = User.objects.get_or_create(username=email, email=email)

            if created:
                user.set_unusable_password()  # Set a placeholder password
                user.save()

            # Generate or update token
            token, created = Token.objects.get_or_create(user=user)
            login(request, user) 
            # Set token expiry time
            token.created = datetime.datetime.now()
            token.save()

            return JsonResponse({
                "message": "OTP verified successfully, user authenticated",
                "token": token.key,  # Send token instead of session key
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                }
            })
        else:
            return JsonResponse({"error": "Invalid or expired OTP"}, status=400)


@csrf_exempt
def send_otp(request):
    if request.method == "POST":
        start_time = time.time() 
        data = json.loads(request.body)
        email = data.get("email")

        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        otp = generate_otp()
        cache.set(email, otp, timeout=300)  # Store OTP for 5 minutes

        try:
            send_otp_email.delay(email, otp)
            end_time = time.time()  # End time after sending email
            total_time = end_time - start_time  # Calculate time taken
            request_count = cache.get("otp_request_count", 0) + 1
            print('time taken',total_time,+request_count)
            return JsonResponse({"message": "OTP sent successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
