# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 02:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_auto_20161113_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistdata',
            old_name='street_address',
            new_name='address',
        ),
    ]
