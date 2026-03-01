"""Eternity Wall provider - ancrage de hash sur la blockchain Bitcoin."""

from __future__ import annotations

from typing import Any

from . import DataIntegrityBaseProvider


class EternityWallProvider(DataIntegrityBaseProvider):
    """Provider Eternity Wall pour l'ancrage de hash sur Bitcoin."""

    name = "eternitywall"
    display_name = "Eternity Wall"
    description = "Ancrage de hash via Eternity Wall (Bitcoin)"
    required_packages = ["requests"]
    documentation_url = "https://eternitywall.it"
    site_url = "https://eternitywall.it"
    config_keys = ["BASE_URL"]
    config_defaults = {
        "BASE_URL": "https://eternitywall.it",
    }
    priority = 4

    def __init__(self, **kwargs: str | None) -> None:
        super().__init__(**kwargs)
        self._base_url = self._get_config_or_env(
            "BASE_URL", "https://eternitywall.it"
        )

    def sign(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError("Eternity Wall ne gère que stamp_hash")

    def stamp_hash(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Ancrer un hash via Eternity Wall."""
        # TODO: intégrer l'API Eternity Wall pour soumettre un hash
        raise NotImplementedError(
            "Implémenter avec l'API Eternity Wall"
        )
