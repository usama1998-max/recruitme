from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import HumanResource, Candidate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .decorators import redirect_on_user_roles


# -------------------- Custom Validation --------------------
def check_user_email(email: str) -> bool:
    try:
        User.objects.get(email=email)
        return True
    except ObjectDoesNotExist:
        return False


# -------------------- HOME VIEW --------------------
def home(request):
    current_user = request.user
    try:
        user_role = request.user.groups.all()[0].name
    except Exception:
        user_role = None
    return render(request, "home.html", {'current_user': current_user,
                                         'role': user_role,
                                         'title': 'Home'})


# -------------------- LOGIN & LOGOUT VIEW --------------------
@csrf_protect
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

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
@csrf_protect
def hr_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            if check_user_email(form.cleaned_data['email']) is True:
                messages.error(request, "Email already exists!")
            else:
                users = form.save()
                group = Group.objects.get(name='HR')
                users.groups.add(group)
                HumanResource.objects.create(user=users)

                messages.success(request, "User successfully created")
                return redirect('login')
        else:
            messages.error(request, form.errors)

    return render(request, "hr_register.html", {'title': 'Register', 'form': form})


# HR Profile View
@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
@redirect_on_user_roles(allowed_group='HR')
def hr_profile(request):
    user_role = None
    try:
        user_role = request.user.groups.all()[0].name
    except Exception:
        user_role = None
    return render(request, "hr_profile.html", {'title': 'Profile',
                                               'current_user': request.user,
                                               'role': user_role})


# -------------------- CANDIDATE VIEWS --------------------
# Candidate Register View
@csrf_protect
def candidate_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            if check_user_email(form.cleaned_data['email']) is True:
                messages.error(request, "Email already exists")
            else:
                users = form.save()

                group = Group.objects.get(name='Candidates')
                users.groups.add(group)
                Candidate.objects.create(user=users)

                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.error(request, form.errors)

    return render(request, "candidate_register.html", {'title': 'Register', 'form': form})


# Candidate Profile View
@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
@redirect_on_user_roles(allowed_group='Candidates')
def candidate_profile(request):
    return render(request, "candidate_profile.html", {'title': 'Profile', 'current_user': request.user})
