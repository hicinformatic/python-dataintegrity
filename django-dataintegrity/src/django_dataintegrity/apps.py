"""Django app configuration."""

from django.apps import AppConfig


class DjangoDataintegrityConfig(AppConfig):
    """Configuration for the django_dataintegrity app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_dataintegrity"
    verbose_name = "Data Integrity"
