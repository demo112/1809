# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


# 创建一个实体类 Publisher
class Publisher(models.Model):
    """
        主键，django默认 自带主键，默认自增
        表示出版社信息，属性如下
    """
    # name: 出版社名称
    name = models.CharField(max_length=30)
    # address出版社所在地址
    address = models.CharField(max_length=200)
    # city： 出版社在城市
    city = models.CharField(max_length=200)
    # country： 出版社在国家
    country = models.CharField(max_length=20)
    # website： 出版社网址
    website = models.URLField()


class Author(models.Model):
    """作者信息"""
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    isActive = models.BooleanField(default=True)


class Book(models.Model):
    """图书信息"""
    title = models.CharField(max_length=30)
    publicate_date = models.DateField()
    isActive = models.BooleanField(default=True)
