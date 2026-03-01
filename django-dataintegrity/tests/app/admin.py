"""Admin for tests.app."""

from django.contrib import admin

from .models import Registry


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ["name", "content_hash", "has_proof", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "content_hash"]

    def has_proof(self, obj):
        return obj.signstamp_id is not None

    has_proof.boolean = True
    has_proof.short_description = "Preuve"
