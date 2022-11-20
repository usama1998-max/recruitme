from django.db.models.signals import post_save
from .models import HumanResource, UserRole, Candidate


def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'HR':
            hr = HumanResource.objects.create(user=instance.user)
            hr.save()
            print("HR Profile + Roles created!")

        if instance.role == 'CANDIDATE':
            cnd = Candidate.objects.create(user=instance.user)
            cnd.save()
            print("Candidate Profile + Roles created!")


post_save.connect(create_profile, sender=UserRole)
