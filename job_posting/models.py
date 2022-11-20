from django.db import models
from django.contrib.auth.models import User


# Assigns Roles to user when registering
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    HR = 'HR'
    CANDIDATE = 'CANDIDATE'
    ADMIN = 'ADMIN'

    user_type = [
        (HR, 'hr'),
        (CANDIDATE, 'candidate'),
        (ADMIN, 'admin')
    ]

    role = models.CharField(max_length=10, choices=user_type)

    def __str__(self):
        return str(self.user)+" ["+str(self.role)+"] "


# HR Model
class HumanResource(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    company_name = models.CharField(max_length=100, blank=True)
    company_logo = models.ImageField(upload_to="company_logos", default='static/img/hr.jpg')

    def __str__(self):
        return str(self.user)+" "+str(self.company_name)


# Candidate Model
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, null=True, unique=True)
    profile_pic = models.ImageField(upload_to="candidate_profile", default="static/img/hr.jpg")
    address = models.CharField(max_length=200, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Name: "+str(self.user)+", date joined: "+str(self.user.date_joined)
