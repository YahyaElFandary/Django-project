# Generated by Django 2.2.5 on 2020-02-02 22:41

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('Bio', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='project1-img')),
                ('Joing_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
