# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 16:35
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
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('pic', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('genre', models.CharField(blank=True, max_length=64, null=True)),
                ('tags', models.CharField(blank=True, max_length=300, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('date_created', models.DateField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('pic', models.ImageField(default='default/fractal.png', upload_to='')),
                ('bio', models.TextField(blank=True, max_length=3000, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('favorite_artists', models.CharField(blank=True, max_length=300, null=True)),
                ('favorite_genres', models.CharField(blank=True, max_length=300, null=True)),
                ('is_artist', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
