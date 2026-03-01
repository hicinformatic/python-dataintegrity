# Generated migration for SignStamp

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SignStamp",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("hash", models.CharField(db_index=True, help_text="Hash du document/registre (SHA-256)", max_length=64, verbose_name="Hash")),
                ("proof_id", models.CharField(db_index=True, help_text="Identifiant unique de la preuve", max_length=255, unique=True, verbose_name="Proof ID")),
                ("provider", models.CharField(db_index=True, help_text="Provider utilisé (opentimestamps, woleet, sigstore, etc.)", max_length=64, verbose_name="Provider")),
                ("sign_signature", models.TextField(blank=True, default="", help_text="Signature électronique (base64)", verbose_name="Signature")),
                ("sign_public_key", models.TextField(blank=True, default="", help_text="Clé publique pour vérification", verbose_name="Clé publique")),
                ("sign_algorithm", models.CharField(blank=True, default="", help_text="Algorithme (RSA, Ed25519, etc.)", max_length=32, verbose_name="Algorithme")),
                ("sign_timestamp", models.DateTimeField(blank=True, null=True, verbose_name="Horodatage signature")),
                ("stamp_proof", models.TextField(blank=True, default="", help_text="Attestation/receipt (hex ou base64)", verbose_name="Preuve")),
                ("stamp_tx_id", models.CharField(blank=True, default="", help_text="ID transaction blockchain", max_length=128, verbose_name="Transaction ID")),
                ("stamp_merkle_root", models.CharField(blank=True, default="", max_length=128, verbose_name="Racine Merkle")),
                ("stamp_blockchain", models.CharField(blank=True, default="", help_text="bitcoin, ethereum, etc.", max_length=32, verbose_name="Blockchain")),
                ("stamp_timestamp", models.DateTimeField(blank=True, null=True, verbose_name="Horodatage ancrage")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "SignStamp",
                "verbose_name_plural": "SignStamps",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="signstamp",
            index=models.Index(fields=["hash", "provider"], name="djdatainte_hash_provider_idx"),
        ),
    ]
