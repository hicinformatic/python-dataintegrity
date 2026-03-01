"""Models for tests.app - exemples d'utilisation de SignStamp."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from djdataintegrity.fields import HashField


class Registry(models.Model):
    """Registre avec preuve d'intégrité (sign + stamp)."""

    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom"),
        help_text=_("Nom du registre"),
    )
    content_hash = HashField(
        verbose_name=_("Hash du contenu"),
        help_text=_("SHA-256 du registre"),
    )
    signstamp = models.OneToOneField(
        "djdataintegrity.SignStamp",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="registry",
        verbose_name=_("Preuve d'intégrité"),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Registre")
        verbose_name_plural = _("Registres")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name
