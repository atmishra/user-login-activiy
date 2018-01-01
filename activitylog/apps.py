from django.apps import AppConfig


class ActivitylogConfig(AppConfig):
    name = 'activitylog'

    def ready(self):
        from .signals import log_user_logged_in_failed, log_user_logged_in_success
