"""Champs pour djdataintegrity."""

from __future__ import annotations

from django.db import models


class HashField(models.CharField):
    """Champ pour stocker un hash SHA-256 (64 caractères hex)."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 64)
        super().__init__(*args, **kwargs)
