# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-16 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20190116_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name', '-id'], 'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]