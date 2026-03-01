"""Manager for dataintegrity providers."""

from djproviderkit.managers import BaseProviderManager


class ProviderManager(BaseProviderManager):
    """Manager for dataintegrity providers."""

    package_name = "dataintegrity"