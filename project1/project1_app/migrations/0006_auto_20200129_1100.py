# Generated by Django 2.2.5 on 2020-01-29 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1_app', '0005_note_fieldname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='FIELDNAME',
            new_name='ImageProfile',
        ),
    ]
