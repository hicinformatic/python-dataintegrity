"""Admin configuration for django_dataintegrity."""

from .provider import ProviderAdmin
from .signstamp import SignStampAdmin

__all__ = ["ProviderAdmin", "SignStampAdmin"]
