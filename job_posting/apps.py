from django.apps import AppConfig
from django.core.signals import request_finished


class JobPostingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_posting'

    def ready(self):
        from . import signals


