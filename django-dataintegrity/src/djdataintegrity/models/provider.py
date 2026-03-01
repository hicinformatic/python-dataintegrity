"""Provider model for dataintegrity providers."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from virtualqueryset.models import VirtualModel
from dataintegrity.providers import DataIntegrityBaseProvider
from djproviderkit.models.service import define_provider_fields, define_service_fields

from ..managers.provider import ProviderManager

services = list(DataIntegrityBaseProvider._default_services_cfg.keys())


@define_provider_fields(primary_key="name")
@define_service_fields(services)
class DataIntegrityProviderModel(VirtualModel):
    """Virtual model for dataintegrity providers."""

    name: models.CharField = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("Provider name (e.g., opentimestamps, woleet)"),
        primary_key=True,
    )

    objects = ProviderManager()

    class Meta:
        managed = False
        app_label = "djdataintegrity"
        verbose_name = _("Data Integrity Provider")
        verbose_name_plural = _("Data Integrity Providers")
        ordering = ["-priority", "name"]

    def __str__(self) -> str:
        return self.display_name or self.name
