from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import HumanResource, UserRole, Candidate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib import messages


# -------------------- Existing User Function --------------------
def check_user_email(email: str) -> bool:
    try:
        User.objects.get(email=email)
        return True
    except ObjectDoesNotExist:
        return False


def check_user_existence(username: str) -> bool:
    try:
        User.objects.get(username=username)
        return True
    except ObjectDoesNotExist:
        return False


# -------------------- HOME VIEW --------------------
def home(request):
    current_user = get_user(request)

    try:
        users = User.objects.get(username=current_user)
        role = UserRole.objects.get(user=users)
    except ObjectDoesNotExist:
        current_user = None
        role = None
    return render(request, "home.html", {'current_user': current_user,
                                         'role': role,
                                         'title': 'Home'})


# -------------------- LOGIN & LOGOUT VIEW --------------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in!")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, "login.html", {'title': 'Login'})


def logout_user(request):
    logout(request)
    return redirect('/')


# -------------------- HR VIEWS --------------------
# HR Registration
def hr_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnf_password = request.POST.get('cnf_password')
        email = request.POST.get('email')

        if check_user_existence(username) is False:

            if check_user_email(email) is False:

                if password != cnf_password:
                    messages.error(request, "Passwords dont match!")

                else:
                    u = User(username=username, password=password, email=email)
                    u.save()

                    ur = UserRole(u.id, role='HR')
                    ur.save()

                    messages.success(request, "User registered, you can now login")

                    return redirect('login')
            else:
                messages.error(request, "User with that email already exists!")
        else:
            messages.error(request, "Username taken! Try different one")

    return render(request, "hr_register.html", {'title': 'Register as Recruiter'})


# HR Profile View
def hr_profile(request):
    return render(request, "hr_profile.html")


# -------------------- CANDIDATE VIEWS --------------------
# Candidate Register View
def candidate_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnf_password = request.POST.get('cnf_password')
        email = request.POST.get('email')

        if check_user_existence(username) is False:
            if check_user_email(email) is False:
                if password != cnf_password:
                    messages.error(request, "Passwords dont match!")
                else:
                    u = User(username=username, password=password, email=email)
                    u.save()

                    ur = UserRole(u.id, role='CANDIDATE')
                    ur.save()

                    messages.success(request, "User registered, you can now login")
                    return redirect('login')
            else:
                messages.error(request, "User with that email already exists!")
        else:
            messages.error(request, "Username taken! Try different one")

    return render(request, "candidate_register.html")


# Candidate Profile View
def candidate_profile(request):

    return render(request, "candidate_profile.html")
