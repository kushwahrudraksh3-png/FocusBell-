from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


import random

from .emailer import otp_email_send

# Create your views here.

def home(request):
    return render(request, 'landingpage.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        
        if password != confirm_password:
            messages.error(request,"Password and Confirm password do not match")
            return redirect("register_page")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register_page")
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address already exists")
            return redirect('register_page')
        
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
            
        messages.success(request, "Account Created Succesfully.please login.")
        return redirect ('login_page')
        
        
    return render(request, 'register.html')

def login_page(request):

    if request.method == 'POST':

        identify = request.POST.get("identify")
        password = request.POST.get("password")

        if not identify or not password:
            messages.error(request, "Please fill all fields")
            return redirect('login_page')

        user_obj = None

        if '@' in identify:
            user_obj = User.objects.filter(email=identify).first()
        else:
            user_obj = User.objects.filter(username=identify).first()

        if user_obj is None:
            messages.error(request, "Account not found. Please register first.")
            return redirect('register_page')
        
        username = user_obj.username

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, "Invalid Email/Username or Password")
        return redirect('login_page')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('home')
    
def profile(request):
    return render(request, 'profile.html')



def forget_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        user = User.objects.filter(email=email).first()

        if user is None:
            messages.error(request, "This email is not registered.")
            return redirect("forget_password")

        otp = random.randint(100000, 999999)

        # OTP and email session me store
        request.session["reset_email"] = email
        request.session["reset_otp"] = str(otp)

        otp_email_send(email, otp)

        messages.success(request, "OTP sent successfully to your email.")
        return redirect("verify_otp")

    return render(request, "forgetpassword.html")



def verify_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp")

        session_otp = request.session.get("reset_otp")

        if session_otp and session_otp == user_otp:
            messages.success(request, "OTP verified successfully")
            return redirect("reset_password")

        messages.error(request, "Invalid OTP")
        return redirect("verify_otp")

    return render(request, "verify_otp.html")


def reset_password(request):
    email = request.session.get("reset_email")

    if not email:
        messages.error(request, "Session expired. Please try again.")
        return redirect("forget_password")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("reset_password")

        user = User.objects.filter(email=email).first()

        user.set_password(new_password)
        user.save()

        # Session clear
        request.session.pop("reset_email", None)
        request.session.pop("reset_otp", None)

        messages.success(request, "Password reset successfully. Please login.")
        return redirect("login_page")

    return render(request, "reset_password.html")