"""OriginStamp provider - ancrage de hash sur blockchain via API."""

from __future__ import annotations

from typing import Any

from . import DataIntegrityBaseProvider


class OriginTimestampProvider(DataIntegrityBaseProvider):
    """Provider OriginStamp pour l'ancrage de hash (Bitcoin, Ethereum)."""

    name = "origintimestamp"
    display_name = "OriginStamp"
    description = "Ancrage de hash via l'API OriginStamp"
    required_packages = ["requests"]
    documentation_url = "https://docs.originstamp.com"
    site_url = "https://originstamp.com"
    config_keys = ["API_KEY", "BASE_URL"]
    config_defaults = {
        "BASE_URL": "https://api.originstamp.org",
        "API_KEY": "",
    }
    priority = 3

    def __init__(self, **kwargs: str | None) -> None:
        super().__init__(**kwargs)
        self._base_url = self._get_config_or_env(
            "BASE_URL", "https://api.originstamp.org"
        )
        self._api_key = self._get_config_or_env("API_KEY", "")

    def sign(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError("OriginStamp ne gère que stamp_hash")

    def stamp_hash(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Ancrer un hash via l'API OriginStamp."""
        # TODO: POST /api/v4/timestamp/create avec hash + API key
        raise NotImplementedError(
            "Implémenter avec requests: POST {base_url}/api/v4/timestamp/create"
        )
