"""Admin for SignStamp model."""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models.signstamp import SignStamp


@admin.register(SignStamp)
class SignStampAdmin(admin.ModelAdmin):
    """Admin for SignStamp."""

    list_display = ["proof_id", "hash", "provider", "has_sign_display", "has_stamp_display", "created_at"]
    list_filter = ["provider", "created_at"]
    search_fields = ["proof_id", "hash", "provider"]
    readonly_fields = ["created_at"]
    fieldsets = (
        (None, {"fields": ("hash", "proof_id", "provider")}),
        (_("Signature"), {"fields": ("sign_signature", "sign_public_key", "sign_algorithm", "sign_timestamp")}),
        (_("Ancrage blockchain"), {"fields": ("stamp_proof", "stamp_tx_id", "stamp_merkle_root", "stamp_blockchain", "stamp_timestamp")}),
        (_("Métadonnées"), {"fields": ("created_at",)}),
    )

    def has_sign_display(self, obj: SignStamp) -> bool:
        return obj.has_sign

    has_sign_display.boolean = True
    has_sign_display.short_description = _("Sign")

    def has_stamp_display(self, obj: SignStamp) -> bool:
        return obj.has_stamp

    has_stamp_display.boolean = True
    has_stamp_display.short_description = _("Stamp")
