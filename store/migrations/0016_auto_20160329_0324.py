# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20160329_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=140, verbose_name='Instagram'),
        ),
    ]
