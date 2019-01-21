# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class AuthorManager(models.Manager):
    def age_count(self, age):
        return self.filter(age__gte=age).count()

    def name_like(self, name):
        author = self.filter(name__contains=name)
        for au in author:
            print("姓名：", au.name)
            print("年龄：", au.age)
            print("邮箱：", au.email)
        return author


class BookManager(models.Manager):
    def book_date(self, year):
        books = self.filter(publicate_date__year=year)
        for book in books:
            print("名称：", book.title)
            print("作者：", book.author_set.values())
            print("出版社：", book.publisher)
            print("出版时间：", book.publicate_date)
        return books


# 创建一个实体类 Publisher
class Publisher(models.Model):
    """
        主键，django默认 自带主键，默认自增
        表示出版社信息，属性如下
    """
    # name: 出版社名称
    name = models.CharField(max_length=100)
    # address出版社所在地址
    address = models.CharField(max_length=200)
    # city： 出版社在城市
    city = models.CharField(max_length=200)
    # country： 出版社在国家
    country = models.CharField(max_length=20)
    # website： 出版社网址
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        # 指定该实体类映射到表的名字,这样的话就不会叫index_author了
        db_table = 'publisher'
        # (该属性设置完成后需要同步回数据库)
        verbose_name = "出版社"
        # 定义实体类在admin中的显示的名字(单数)
        # 定义实体类在admin中的显示的名字(复数)
        verbose_name_plural = verbose_name
        # 指定数据在后台管理界面中的排序方式
        ordering = ['name', '-id']


class Author(models.Model):
    """作者信息"""
    objects = AuthorManager()
    name = models.CharField(max_length=100, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(null=True, verbose_name="邮箱")
    isActive = models.BooleanField(default=True, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        # 指定该实体类映射到表的名字,这样的话就不会叫index_author了
        db_table = 'author'
        # (该属性设置完成后需要同步回数据库)
        verbose_name = "作者"
        # 定义实体类在admin中的显示的名字(单数)
        # 定义实体类在admin中的显示的名字(复数)
        verbose_name_plural = verbose_name
        # 指定数据在后台管理界面中的排序方式
        ordering = ['age', '-id']


class Book(models.Model):
    """图书信息"""
    objects = BookManager()
    title = models.CharField(max_length=100, verbose_name="书名")
    publicate_date = models.DateField(verbose_name="出版时间")
    isActive = models.BooleanField(default=True, verbose_name="状态")
    # 添加对Publisher（一）的引用关系
    publisher = models.ForeignKey(Publisher, null=True, verbose_name="出版社")
    author_set = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        # 指定该实体类映射到表的名字,这样的话就不会叫index_author了
        db_table = 'book'
        # (该属性设置完成后需要同步回数据库)
        verbose_name = "书籍"
        # 定义实体类在admin中的显示的名字(单数)
        # 定义实体类在admin中的显示的名字(复数)
        verbose_name_plural = verbose_name
        # 指定数据在后台管理界面中的排序方式
        ordering = ['-publicate_date', '-id']


class Wife(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    author = models.OneToOneField(Author, null=True, verbose_name='丈夫（作者）')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = "夫人"
        verbose_name_plural = verbose_name
