"""Pytest configuration for django-dataintegrity."""

import pytest


@pytest.fixture(scope="session")
def django_db_setup():
    """Use in-memory SQLite for tests."""
    pass
