# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20161113_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
