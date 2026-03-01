"""SignStamp model - signature et/ou ancrage blockchain pour preuve d'intégrité."""

from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _


class SignStamp(models.Model):
    """Preuve d'intégrité : signature et/ou ancrage blockchain.

    Permet sign seul, stamp_hash seul, ou les deux (double sécurité).
    Exemple : signer un registre puis ancrer le hash = double preuve.
    """

    hash = models.CharField(
        max_length=64,
        verbose_name=_("Hash"),
        help_text=_("Hash du document/registre (SHA-256)"),
        db_index=True,
    )
    proof_id = models.CharField(
        max_length=255,
        verbose_name=_("Proof ID"),
        help_text=_("Identifiant unique de la preuve"),
        unique=True,
        db_index=True,
    )
    provider = models.CharField(
        max_length=64,
        verbose_name=_("Provider"),
        help_text=_("Provider utilisé (opentimestamps, woleet, sigstore, etc.)"),
        db_index=True,
    )

    # Signature électronique (optionnel)
    sign_signature = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Signature"),
        help_text=_("Signature électronique (base64)"),
    )
    sign_public_key = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Clé publique"),
        help_text=_("Clé publique pour vérification"),
    )
    sign_algorithm = models.CharField(
        max_length=32,
        blank=True,
        default="",
        verbose_name=_("Algorithme"),
        help_text=_("Algorithme (RSA, Ed25519, etc.)"),
    )
    sign_timestamp = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Horodatage signature"),
    )

    # Ancrage blockchain (optionnel)
    stamp_proof = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Preuve"),
        help_text=_("Attestation/receipt (hex ou base64)"),
    )
    stamp_tx_id = models.CharField(
        max_length=128,
        blank=True,
        default="",
        verbose_name=_("Transaction ID"),
        help_text=_("ID transaction blockchain"),
    )
    stamp_merkle_root = models.CharField(
        max_length=128,
        blank=True,
        default="",
        verbose_name=_("Racine Merkle"),
    )
    stamp_blockchain = models.CharField(
        max_length=32,
        blank=True,
        default="",
        verbose_name=_("Blockchain"),
        help_text=_("bitcoin, ethereum, etc."),
    )
    stamp_timestamp = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Horodatage ancrage"),
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("SignStamp")
        verbose_name_plural = _("SignStamps")
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["hash", "provider"]),
        ]

    def __str__(self) -> str:
        parts = [self.proof_id]
        if self.has_sign:
            parts.append("✓sign")
        if self.has_stamp:
            parts.append("✓stamp")
        return " ".join(parts)

    @property
    def has_sign(self) -> bool:
        return bool(self.sign_signature)

    @property
    def has_stamp(self) -> bool:
        return bool(self.stamp_proof or self.stamp_tx_id)
