from django.contrib import admin
from .models import HumanResource, UserRole, Candidate

# Register your models here.
admin.site.register(UserRole)
admin.site.register(Candidate)
admin.site.register(HumanResource)
