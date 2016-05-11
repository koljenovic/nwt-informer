# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20160330_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=200)),
                ('adresa', models.CharField(max_length=200)),
                ('pdv_broj', models.CharField(max_length=25)),
                ('id_broj', models.CharField(max_length=25)),
                ('admin_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50)),
                ('postanski_broj', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kontakt', models.CharField(max_length=250)),
                ('firma_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_registracije', models.DateTimeField(auto_now_add=True)),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
                ('slika', models.CharField(max_length=250)),
                ('firma_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Uloga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv_uloge', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VrstaKontakta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vrsta_kontakta', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='adresarfirmastavkaregistar',
            name='korisnikregistar_fk',
        ),
        migrations.RemoveField(
            model_name='adresarlicestavkaregistar',
            name='korisnikregistar_fk',
        ),
        migrations.RemoveField(
            model_name='firmaregistar',
            name='korisnikregistar_fk',
        ),
        migrations.RemoveField(
            model_name='korisnikregistar',
            name='korisnikregistar_fk',
        ),
        migrations.DeleteModel(
            name='AdresarFirmaStavkaRegistar',
        ),
        migrations.DeleteModel(
            name='AdresarLiceStavkaRegistar',
        ),
        migrations.DeleteModel(
            name='FirmaRegistar',
        ),
        migrations.DeleteModel(
            name='KorisnikRegistar',
        ),
        migrations.DeleteModel(
            name='UserRegistar',
        ),
        migrations.AddField(
            model_name='osoba',
            name='uloga_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Uloga'),
        ),
        migrations.AddField(
            model_name='osoba',
            name='user_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='osoba_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Osoba'),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='vrsta_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.VrstaKontakta'),
        ),
        migrations.AddField(
            model_name='firma',
            name='grad_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Grad'),
        ),
        migrations.AddField(
            model_name='firma',
            name='uloga_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Uloga'),
        ),
        migrations.AddField(
            model_name='adresar',
            name='kontakt_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Kontakt'),
        ),
        migrations.AddField(
            model_name='adresar',
            name='osoba_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Osoba'),
        ),
    ]