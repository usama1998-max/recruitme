from django.contrib import admin
from .models import HumanResource, Candidate, JobPost, CandidatesWhoApplied


# Register your models here.
admin.site.register(Candidate)
admin.site.register(HumanResource)
admin.site.register(JobPost)
admin.site.register(CandidatesWhoApplied)
