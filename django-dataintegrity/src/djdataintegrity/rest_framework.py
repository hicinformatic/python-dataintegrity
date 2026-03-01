"""Champs Django REST Framework pour djdataintegrity."""

from rest_framework import serializers


class SignStampField(serializers.JSONField):
    """Champ sérializer pour SignStamp."""

    def __init__(self, **kwargs):
        kwargs.setdefault("help_text", "Preuve d'intégrité (signature et/ou ancrage)")
        super().__init__(**kwargs)
