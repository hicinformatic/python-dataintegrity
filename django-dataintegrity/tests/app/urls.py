"""URLs for tests.app."""

from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.registry_list, name="registry_list"),
]
