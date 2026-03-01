# Migration to rename app from djdataintegrity to django_dataintegrity (existing installations)

from django.db import migrations


def rename_tables(apps, schema_editor):
    """Rename djdataintegrity_* tables to django_dataintegrity_* (existing installs only)."""
    from django.db import connection

    vendor = connection.vendor
    with connection.cursor() as cursor:
        if vendor == "postgresql":
            cursor.execute(
                """
                SELECT tablename FROM pg_tables
                WHERE schemaname = 'public' AND tablename LIKE 'djdataintegrity_%'
                """
            )
            tables = [row[0] for row in cursor.fetchall()]
        elif vendor == "sqlite":
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'djdataintegrity_%'"
            )
            tables = [row[0] for row in cursor.fetchall()]
        else:
            return

        if not tables:
            return

        for old_name in tables:
            new_name = old_name.replace("djdataintegrity_", "django_dataintegrity_", 1)
            if vendor == "postgresql":
                cursor.execute(f'ALTER TABLE "{old_name}" RENAME TO "{new_name}"')
            else:
                cursor.execute(f'ALTER TABLE "{old_name}" RENAME TO "{new_name}"')

        cursor.execute(
            "UPDATE django_content_type SET app_label = 'django_dataintegrity' WHERE app_label = 'djdataintegrity'"
        )
        cursor.execute(
            "UPDATE django_migrations SET app = 'django_dataintegrity' WHERE app = 'djdataintegrity'"
        )


def reverse_rename(apps, schema_editor):
    """Reverse: rename django_dataintegrity_* back to djdataintegrity_*."""
    from django.db import connection

    vendor = connection.vendor
    with connection.cursor() as cursor:
        if vendor == "postgresql":
            cursor.execute(
                "SELECT tablename FROM pg_tables WHERE schemaname = 'public' AND tablename LIKE 'django_dataintegrity_%'"
            )
        elif vendor == "sqlite":
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'django_dataintegrity_%'"
            )
        else:
            return
        tables = [row[0] for row in cursor.fetchall()]

        for old_name in tables:
            new_name = old_name.replace("django_dataintegrity_", "djdataintegrity_", 1)
            cursor.execute(f'ALTER TABLE "{old_name}" RENAME TO "{new_name}"')

        cursor.execute(
            "UPDATE django_content_type SET app_label = 'djdataintegrity' WHERE app_label = 'django_dataintegrity'"
        )
        cursor.execute(
            "UPDATE django_migrations SET app = 'djdataintegrity' WHERE app = 'django_dataintegrity'"
        )


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.RunPython(rename_tables, reverse_rename),
    ]
