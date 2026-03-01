"""Woleet provider - ancrage et signature (Proof of Timestamp, Proof of Seal)."""

from __future__ import annotations

from typing import Any

from . import DataIntegrityBaseProvider


class WoleetProvider(DataIntegrityBaseProvider):
    """Provider Woleet : ancrage blockchain et proof of seal (signature)."""

    name = "woleet"
    display_name = "Woleet"
    description = "Ancrage hash et proof of seal via l'API Woleet"
    required_packages = ["requests"]
    documentation_url = "https://doc.woleet.io"
    site_url = "https://www.woleet.io"
    config_keys = ["API_KEY", "BASE_URL"]
    config_defaults = {
        "BASE_URL": "https://api.woleet.io",
        "API_KEY": "",
    }
    priority = 2

    def __init__(self, **kwargs: str | None) -> None:
        super().__init__(**kwargs)
        self._base_url = self._get_config_or_env(
            "BASE_URL", "https://api.woleet.io"
        )
        self._api_key = self._get_config_or_env("API_KEY", "")

    def sign(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Proof of Seal : signer le hash (nécessite clé privée / API)."""
        # TODO: Proof of Seal - hash + public_key + signature
        raise NotImplementedError(
            "Implémenter Proof of Seal avec l'API Woleet"
        )

    def stamp_hash(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Proof of Timestamp : ancrer le hash sur Bitcoin."""
        # TODO: POST /v1/anchor - créer un anchor à partir du hash
        raise NotImplementedError(
            "Implémenter avec POST {base_url}/v1/anchor"
        )
