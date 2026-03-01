"""URL configuration for testing django-dataintegrity."""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/django_dataintegrity/", permanent=False)),
    path("admin/", admin.site.urls),
    path("django_dataintegrity/", include("django_dataintegrity.urls")),
    path("registries/", include("tests.app.urls")),
]
