"""Django DataIntegrity - Preuve d'intégrité (signature, ancrage blockchain) pour Django."""

from __future__ import annotations

from django.db import models

__version__ = "0.1.0"

default_app_config = "djdataintegrity.apps.DjDataIntegrityConfig"

fields_associations = {
    'int': models.IntegerField,
    'float': models.FloatField,
    'bool': models.BooleanField,
    'list': models.JSONField,
    'str': models.CharField,
    'text': models.TextField,
    'date': models.DateField,
    'time': models.TimeField,
    'datetime': models.DateTimeField,
    'email': models.EmailField,
    'url': models.URLField,
}
