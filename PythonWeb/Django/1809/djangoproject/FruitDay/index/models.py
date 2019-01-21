from django.db import models


# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=11, verbose_name='手机号码')
    upwd = models.CharField(max_length=200, verbose_name='密码')
    uemail = models.CharField(max_length=245, verbose_name='邮箱')
    uname = models.CharField(max_length=20, verbose_name='用户名')
    isActive = models.BooleanField(default=True, verbose_name='状态')

    def __str__(self):
        return self.uname

    class META:
        db_tabble = 'users'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
