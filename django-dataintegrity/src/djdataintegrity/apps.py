"""Django app configuration."""

from django.apps import AppConfig


class DjDataIntegrityConfig(AppConfig):
    """Configuration for the djdataintegrity app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "djdataintegrity"
    verbose_name = "Data Integrity"
