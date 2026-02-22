"""OpenTimestamps provider - ancrage de hash sur la blockchain Bitcoin."""

from __future__ import annotations

from typing import Any

from . import DataIntegrityBaseProvider


class OpenTimestampsProvider(DataIntegrityBaseProvider):
    """Provider OpenTimestamps pour l'ancrage de hash sur Bitcoin."""

    name = "opentimestamps"
    display_name = "OpenTimestamps"
    description = "Ancrage de hash via le protocole OpenTimestamps (Bitcoin)"
    required_packages = ["opentimestamps-client"]
    documentation_url = "https://opentimestamps.org"
    site_url = "https://opentimestamps.org"
    config_keys = ["CALENDAR_URL"]
    config_defaults = {
        "CALENDAR_URL": "https://calendar.opentimestamps.org",
    }
    priority = 2

    def __init__(self, **kwargs: str | None) -> None:
        super().__init__(**kwargs)
        self._calendar_url = self._get_config_or_env(
            "CALENDAR_URL", "https://calendar.opentimestamps.org"
        )

    def sign(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError("OpenTimestamps ne gère que stamp_hash")

    def stamp_hash(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Ancrer un hash via OpenTimestamps. Utilise opentimestamps-client (ots stamp)."""
        # TODO: intégrer opentimestamps-client (ots stamp <hash>) ou python-opentimestamps
        raise NotImplementedError(
            "Implémenter avec opentimestamps-client: ots stamp <fichier>"
        )
