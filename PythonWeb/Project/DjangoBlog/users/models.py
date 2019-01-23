# coding=utf-8
from django.db import models


# Create your models here.
from topic.models import Topic


class Reply(models.Model):
    content = models.TextField(null=False)
    reply_time = models.DateTimeField(null=False)
    # user = models.OneToOneField(User, null=True, verbose_name='回复ID')
    # topic = models.OneToOneField(Topic, null=True, verbose_name='回复帖子')
    
    def __str__(self):
        return self.content


class User(models.Model):
    pass

class Voke(models.Model):
    pass
