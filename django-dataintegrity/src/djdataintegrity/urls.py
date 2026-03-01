"""URL configuration for django-dataintegrity."""

from django.urls import path

from .views.provider import list_providers, detail_provider
from .views.index import index

app_name = "djdataintegrity"

urlpatterns = [
    path("", index, name="index"),
    path("providers/<str:provider_name>/", detail_provider, name="detail_provider"),
    path("providers/", list_providers, name="list_providers"),
]
