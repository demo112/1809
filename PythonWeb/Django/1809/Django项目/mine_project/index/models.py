# coding=utf-8
from django.db import models

# Create your models here.


class Users(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    uage = models.IntegerField()
    uemail = models.CharField(max_length=30)

    def __str__(self):
        return self.uname

    class META:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
