# coding=utf-8
from django.db import models

# Create your models here.


class Blogtype(models.Model):
    """博客种类"""
    type_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.type_name

    class META:
        db_table = 'blogtype'
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name
    pass


class Category(models.Model):
    """博客种类"""
    cate_name = models.CharField(max_length=50, null=False)
    pass


class Topic(models.Model):
    pass
