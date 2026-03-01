"""View for dataintegrity home page."""

from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from . import dataintegrityview_enabled_and_login


@dataintegrityview_enabled_and_login("DATAINTEGRITY_PROVIDERVIEW")
def index(request: HttpRequest) -> HttpResponse:
    """Home page for dataintegrity with links to providers."""

    context = {
        "providers_url": reverse("djdataintegrity:list_providers"),
    }
    return render(request, "djdataintegrity/index.html", context)
