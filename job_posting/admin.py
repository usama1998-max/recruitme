from django.contrib import admin
from .models import HumanResource, Candidate, JobPost


# Register your models here.
admin.site.register(Candidate)
admin.site.register(HumanResource)
admin.site.register(JobPost)
