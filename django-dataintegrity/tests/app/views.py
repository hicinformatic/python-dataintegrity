"""Views for tests.app."""

from django.shortcuts import render

from .models import Registry


def registry_list(request):
    """Liste des registres avec preuves."""
    registries = Registry.objects.select_related("signstamp").all()
    return render(request, "app/registry_list.html", {"registries": registries})
