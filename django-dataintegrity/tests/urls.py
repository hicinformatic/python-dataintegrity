"""URL configuration for testing django-dataintegrity."""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/djdataintegrity/", permanent=False)),
    path("admin/", admin.site.urls),
    path("djdataintegrity/", include("djdataintegrity.urls")),
    path("registries/", include("tests.app.urls")),
]
