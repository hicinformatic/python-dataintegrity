# Generated migration for tests.app

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("djdataintegrity", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="Nom du registre", max_length=255, verbose_name="Nom")),
                ("content_hash", models.CharField(help_text="SHA-256 du registre", max_length=64, verbose_name="Hash du contenu")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("signstamp", models.OneToOneField(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name="registry",
                    to="djdataintegrity.signstamp",
                    verbose_name="Preuve d'intégrité",
                )),
            ],
            options={
                "verbose_name": "Registre",
                "verbose_name_plural": "Registres",
                "ordering": ["-created_at"],
            },
        ),
    ]
