# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-16 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20190116_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['age', '-id'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
    ]
