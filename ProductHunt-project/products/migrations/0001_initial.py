# Generated by Django 2.2.5 on 2020-02-22 13:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('url', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('votes_total', models.IntegerField(blank=True, default=1)),
                ('image', models.ImageField(height_field=600, upload_to='media', width_field=700)),
                ('icon', models.ImageField(height_field=300, upload_to='media', width_field=300)),
                ('body', models.TextField()),
                ('pub_date_pretty', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
