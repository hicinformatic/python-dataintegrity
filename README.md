# DataIntegrity

Monorepo contenant **dataintegrity** (bibliothèque Python pour la preuve d'intégrité) et **django-dataintegrity** (intégration Django).

## Packages

### dataintegrity — `python-dataintegrity/`

Bibliothèque Python pour la gestion des fournisseurs de preuve d'intégrité via hash (blockchain) ou signature.

- **Preuve d'intégrité** : hash, blockchain, signature
- **Vérification** : validation des données
- **ProviderKit** : architecture multi-providers

📁 Docs : [python-dataintegrity/docs/](python-dataintegrity/docs/)

### django-dataintegrity — `django-dataintegrity/`

Intégration Django pour la preuve d'intégrité : champs, widgets, admin.

📁 Docs : [django-dataintegrity/docs/](django-dataintegrity/docs/)

## Structure du dépôt

```
dataintegrity/
├── python-dataintegrity/   # Bibliothèque core
├── django-dataintegrity/  # Intégration Django
└── README.md
```

## Développement

Chaque package a son propre `service.py` :

```bash
# Dans python-dataintegrity/ ou django-dataintegrity/
./service.py dev install-dev
./service.py dev test
./service.py quality lint
```

## Licence

MIT
