# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160531_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontakt',
            name='osoba_fk',
        ),
        migrations.AddField(
            model_name='kontakt',
            name='kategorija',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='naziv',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]