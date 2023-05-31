from django.apps import AppConfig


class UsersProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users_profile"

    def ready(self):
        import users_profile.signals