# Generated manually to fix Render deployment issue

from django.db import migrations


def drop_quizsettings_table_if_exists(apps, schema_editor):
    """
    Safely drop the quiz_quizsettings table if it exists.
    This handles the case where the table exists in the database
    but the migration history is inconsistent.
    """
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("""
            DROP TABLE IF EXISTS quiz_quizsettings;
        """)


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_delete_quizsettings'),
    ]

    operations = [
        migrations.RunPython(drop_quizsettings_table_if_exists, migrations.RunPython.noop),
    ]
