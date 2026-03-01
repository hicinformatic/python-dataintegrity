"""Providers for integrity proof: electronic signature and blockchain hash."""

from __future__ import annotations

from typing import Any

from providerkit import ProviderBase

# Champs communs aux preuves d'intégrité
FIELDS_INTEGRITY_BASE = {
    "hash": {
        "label": "Hash",
        "description": "Hash du document (SHA-256)",
        "format": "str",
    },
    "proof_id": {
        "label": "Proof ID",
        "description": "Identifiant unique de la preuve",
        "format": "str",
    },
}

# Champs pour la signature électronique
FIELDS_SIGNATURE = {
    **FIELDS_INTEGRITY_BASE,
    "signature": {
        "label": "Signature",
        "description": "Signature électronique (base64)",
        "format": "str",
    },
    "public_key": {
        "label": "Clé publique",
        "description": "Clé publique pour vérification",
        "format": "str",
    },
    "algorithm": {
        "label": "Algorithme",
        "description": "Algorithme de signature (ex: RSA, Ed25519)",
        "format": "str",
    },
    "timestamp": {
        "label": "Horodatage",
        "description": "Date/heure de la signature",
        "format": "str",
    },
}

# Champs pour le hash blockchain (ex: OpenTimestamps)
FIELDS_BLOCKCHAIN_HASH = {
    **FIELDS_INTEGRITY_BASE,
    "proof": {
        "label": "Preuve",
        "description": "Preuve d'existence (attestation ou receipt)",
        "format": "str",
    },
    "tx_id": {
        "label": "Transaction ID",
        "description": "ID de transaction blockchain",
        "format": "str",
    },
    "merkle_root": {
        "label": "Racine Merkle",
        "description": "Racine de l'arbre Merkle ancré",
        "format": "str",
    },
    "blockchain": {
        "label": "Blockchain",
        "description": "Blockchain utilisée (ex: bitcoin)",
        "format": "str",
    },
    "timestamp": {
        "label": "Horodatage",
        "description": "Date/heure attestée",
        "format": "str",
    },
}


class DataIntegrityBaseProvider(ProviderBase):
    """Base class for integrity proof providers.

    Two service types:
    - sign: electronic signature (document hash → signed proof)
    - stamp_hash: blockchain anchor (hash → OpenTimestamps-like proof)
    """

    name = "dataintegrity"
    display_name = "Data Integrity"
    description = "Preuve d'intégrité via signature ou hash blockchain"
    required_packages = ["dataintegrity"]
    config_prefix = "DATAINTEGRITY"
    config_keys: list[str] = []
    config_defaults: dict[str, Any] = {}
    provider_key = "key"

    _default_services_cfg = {
        "sign": {
            "label": "Signature électronique",
            "description": "Signer un hash de document",
            "fields": FIELDS_SIGNATURE,
        },
        "stamp_hash": {
            "label": "Ancrage blockchain",
            "description": "Ancrer un hash sur blockchain (ex: OpenTimestamps)",
            "fields": FIELDS_BLOCKCHAIN_HASH,
        },
    }

    def sign(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Signer un hash de document. À surcharger par les providers."""
        raise NotImplementedError

    def stamp_hash(self, document_hash: str, **kwargs: Any) -> dict[str, Any]:
        """Ancrer un hash sur blockchain. À surcharger par les providers."""
        raise NotImplementedError


from .eternitywall import EternityWallProvider
from .opentimestamps import OpenTimestampsProvider
from .origintimestamp import OriginTimestampProvider
from .sigstore import SigstoreProvider
from .woleet import WoleetProvider

__all__ = [
    "DataIntegrityBaseProvider",
    "EternityWallProvider",
    "FIELDS_BLOCKCHAIN_HASH",
    "FIELDS_INTEGRITY_BASE",
    "FIELDS_SIGNATURE",
    "OpenTimestampsProvider",
    "OriginTimestampProvider",
    "SigstoreProvider",
    "WoleetProvider",
]
