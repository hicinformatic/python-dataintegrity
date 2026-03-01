"""Tests pour djdataintegrity."""

import pytest
from django.test import TestCase

from djdataintegrity.models import SignStamp


@pytest.mark.django_db
class TestSignStampModel(TestCase):
    """Tests du modèle SignStamp."""

    def test_create_sign_only(self):
        """Création SignStamp avec signature uniquement."""
        ss = SignStamp.objects.create(
            hash="a" * 64,
            proof_id="test-sign-001",
            provider="sigstore",
            sign_signature="base64sig...",
            sign_public_key="pk...",
            sign_algorithm="Ed25519",
        )
        assert ss.has_sign is True
        assert ss.has_stamp is False
        assert "✓sign" in str(ss)

    def test_create_stamp_only(self):
        """Création SignStamp avec ancrage uniquement."""
        ss = SignStamp.objects.create(
            hash="b" * 64,
            proof_id="test-stamp-001",
            provider="opentimestamps",
            stamp_proof="0x...",
            stamp_blockchain="bitcoin",
        )
        assert ss.has_sign is False
        assert ss.has_stamp is True
        assert "✓stamp" in str(ss)

    def test_create_both(self):
        """Création SignStamp avec sign + stamp (double sécurité)."""
        ss = SignStamp.objects.create(
            hash="c" * 64,
            proof_id="test-both-001",
            provider="woleet",
            sign_signature="sig...",
            stamp_proof="proof...",
            stamp_blockchain="bitcoin",
        )
        assert ss.has_sign is True
        assert ss.has_stamp is True
