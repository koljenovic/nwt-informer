# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_osoba_datum_registracije'),
    ]

    operations = [
        migrations.AddField(
            model_name='firma',
            name='slika',
            field=models.ImageField(default=datetime.datetime(2016, 5, 24, 18, 30, 49, 929276, tzinfo=utc), upload_to='documents/'),
            preserve_default=False,
        ),
    ]
