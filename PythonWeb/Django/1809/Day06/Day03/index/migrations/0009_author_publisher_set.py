# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-21 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_book_author_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publisher_set',
            field=models.ManyToManyField(to='index.Publisher'),
        ),
    ]
