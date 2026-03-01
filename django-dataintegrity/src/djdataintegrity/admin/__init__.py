"""Admin configuration for djdataintegrity."""

from .provider import ProviderAdmin
from .signstamp import SignStampAdmin

__all__ = ["ProviderAdmin", "SignStampAdmin"]
