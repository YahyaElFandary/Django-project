# Generated by Django 2.2.5 on 2020-01-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1_app', '0004_auto_20200128_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='FIELDNAME',
            field=models.ImageField(default='', upload_to='project1-img'),
            preserve_default=False,
        ),
    ]
