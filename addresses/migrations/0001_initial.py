# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=128, verbose_name='Address lines 1')),
                ('address2', models.CharField(blank=True, max_length=128, verbose_name='Address lines 2')),
                ('city', models.CharField(max_length=64, verbose_name='City')),
                ('state', localflavor.us.models.USStateField(max_length=2, verbose_name='State')),
                ('zipcode', models.CharField(max_length=5, verbose_name='Zipcode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]
