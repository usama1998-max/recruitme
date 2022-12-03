from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import HumanResource, Candidate, JobPost
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import CreateUserForm, HRProfile, UserUpdateForm, CandidateProfile, CreateJobPost
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .decorators import redirect_on_user_roles
from django.urls import reverse


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
    form = UserUpdateForm()
    hr_form = HRProfile()
    company_image = None
    profile_image = None

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        hr_form = HRProfile(request.POST, files=request.FILES, instance=request.user.humanresource)
        print(request.FILES)
        if form.is_valid() and hr_form.is_valid():
            form.save()
            hr_form.save()
            messages.success(request, "Updated")
        else:
            messages.error(request, form.errors)
    else:
        form = UserUpdateForm(instance=request.user)
        hr_form = HRProfile(instance=request.user.humanresource)
        company_image = request.user.humanresource.company_logo.url
        profile_image = request.user.humanresource.profile_pic.url

    try:
        user_role = request.user.groups.all()[0].name
    except Exception:
        user_role = None
    return render(request, "hr_profile.html", {'title': 'Profile',
                                               'current_user': request.user,
                                               'role': user_role,
                                               'form': form,
                                               'hr_form': hr_form,
                                               'company_image': company_image,
                                               'profile_image': profile_image})


@login_required(login_url=settings.LOGIN_URL)
def about_hr(request, user):
    current_user = User.objects.get(username=user)

    role = None

    if current_user.groups.all()[0].name:
        role = current_user.groups.all()[0].name

    return render(request, "hr.html", {'title': 'About',
                                       'current_user': current_user,
                                       'role': role})


@login_required(login_url=settings.LOGIN_URL)
@redirect_on_user_roles(allowed_group='HR')
def dashboard(request):
    current_user = request.user
    role = current_user.groups.all()[0].name
    return render(request, "dashboard.html", {'current_user': current_user,
                                              'role': role})


# -------------------- COMPANY VIEWS --------------------
@login_required(login_url=settings.LOGIN_URL)
def about_company(request, user):

    company = HumanResource.objects.get(user=User.objects.get(username=user).id)
    current_user = request.user

    return render(request, "about_company.html", {'title': company.company_name,
                                                  'company': company,
                                                  'current_user': current_user})


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
    user_role = None
    form = UserUpdateForm()
    c_form = CandidateProfile()
    profile_image = None

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        c_form = CandidateProfile(request.POST, files=request.FILES, instance=request.user.candidate)

        if form.is_valid() and c_form.is_valid():
            form.save()
            c_form.save()
            messages.success(request, "Updated")
        else:
            messages.error(request, form.errors)
    else:
        form = UserUpdateForm(instance=request.user)
        c_form = CandidateProfile(instance=request.user.candidate)
        profile_image = request.user.candidate.profile_pic.url

    try:
        user_role = request.user.groups.all()[0].name
    except Exception:
        user_role = None
    return render(request, "candidate_profile.html", {'title': 'Profile',
                                                      'current_user': request.user,
                                                      'role': user_role,
                                                      'form': form,
                                                      'c_form': c_form,
                                                      'profile_image': profile_image,})


@login_required(login_url=settings.LOGIN_URL)
def about_candidate(request):
    current_user = request.user
    role = None
    if current_user.groups.all()[0].name:
        role = current_user.groups.all()[0].name
    print(role)
    return render(request, "candidate.html", {'title': 'About',
                                              'current_user': current_user,
                                              'role': role})


# -------------------- JOB VIEWS --------------------
def jobs(request):
    current_user = request.user
    job = JobPost.objects.all()
    return render(request, "jobs.html", {'title': 'jobs',
                                         'job': job,
                                         'current_user': current_user})


def create_job(request):
    cjp = CreateJobPost()

    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        hr = HumanResource.objects.get(user=user)

        cjp = CreateJobPost(request.POST)

        if cjp.is_valid():
            JobPost.objects.create(user=hr, title=cjp.cleaned_data['title'], description=cjp.cleaned_data['description'])
            messages.success(request, 'Post created')
            return redirect('jobs')
        else:
            messages.error(request, cjp.errors)

    return render(request, "create_job.html", {'title': 'Post Job',
                                               'cjp': cjp})


@login_required(login_url=settings.LOGIN_URL)
def view_job(request, pk):
    current_user = request.user
    j = JobPost.objects.get(id=pk)
    return render(request, "view_job.html", {'current_user': current_user,
                                             'job': j})



