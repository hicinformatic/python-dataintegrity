"""Sigstore provider - signature électronique pour artefacts logiciels."""

from __future__ import annotations

from typing import Any

from . import DataIntegrityBaseProvider


class SigstoreProvider(DataIntegrityBaseProvider):
    """Provider Sigstore pour la signature d'artefacts (OIDC + transparency log)."""

    name = "sigstore"
    display_name = "Sigstore"
    description = "Signature d'artefacts via Sigstore (OIDC, Rekor)"
    required_packages = ["sigstore"]
    documentation_url = "https://sigstore.github.io/sigstore-python/"
    site_url = "https://sigstore.dev"
    config_keys = ["OIDC_ISSUER", "FULCIO_URL", "REKOR_URL"]
    config_defaults = {
        "OIDC_ISSUER": "https://oauth2.sigstore.dev/auth",
        "FULCIO_URL": "https://fulcio.sigstore.dev",
        "REKOR_URL": "https://rekor.sigstore.dev",
    }
    priority = 1

    def __init__(self, **kwargs: str | None) -> None:
        super().__init__(**kwargs)
        self._oidc_issuer = self._get_config_or_env(
            "OIDC_ISSUER", "https://oauth2.sigstore.dev/auth"
        )

    def sign(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Signer un artefact (ou son hash) via Sigstore."""
        # TODO: SigningContext + signer.sign_artifact() ou sign_hash()
        # Sigstore signe typiquement le fichier, pas juste le hash
        raise NotImplementedError(
            "Implémenter avec sigstore.sign.SigningContext et signer.sign_artifact"
        )

    def stamp_hash(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError("Sigstore ne gère que sign (transparency log inclus)")
