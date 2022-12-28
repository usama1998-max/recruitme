from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# HR Model
class HumanResource(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    company_name = models.CharField(max_length=100, blank=True)
    company_logo = models.ImageField(upload_to="company_logos", default='default_img/default_company_logo.png')
    profile_pic = models.ImageField(upload_to="hr_profile_pic", default='default_img/hr.jpg')

    def __str__(self):
        return str(self.user)

    def __int__(self):
        return int(self.user.id)


# Candidate Model
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, null=True, unique=True)
    profile_pic = models.ImageField(upload_to="candidate_profile", default="default_img/hr.jpg")
    address = models.CharField(max_length=200, null=True, blank=True)
    cv = models.FileField(upload_to="cvs")

    def __str__(self):
        return str(self.user)


class JobPost(models.Model):
    user = models.ForeignKey(HumanResource, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.title)

    def __int__(self):
        return int(self.id)


class CandidatesWhoApplied(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    cv = models.FileField(upload_to="resume")

    def __str__(self):
        return str(self.full_name)
