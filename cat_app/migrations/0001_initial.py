# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-17 21:45
from __future__ import unicode_literals

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
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofileinfos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
