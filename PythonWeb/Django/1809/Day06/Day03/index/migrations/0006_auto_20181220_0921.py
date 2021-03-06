# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-20 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20181220_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'wife',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-age'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='author',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='有效用户'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='wife',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Author'),
        ),
    ]
