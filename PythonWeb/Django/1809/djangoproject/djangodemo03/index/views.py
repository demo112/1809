# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from pymysql import Date

from . import models


# Create your views here.
def add_author(request):
    # way1
    models.Author.objects.create(
        name='屈亚伟',
        age='18',
        email='quyawei@163.com'
    )
    # way2
    author = models.Author(name="王通", age=20)
    author.email = "wangtong@163.com"
    author.save()
    # way3
    dic = {
        'name': '温宇华',
        'age': '22',
        'email': 'wenyuhua@163.com'
    }
    author1 = models.Author(**dic)
    author1.save()
    return HttpResponse(
        '<script>alert("增加成功");</script>'
    )


def add_book(request):
    # way1
    models.Book.objects.create(
        title='红楼梦',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='水浒传',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='西游记',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='三国演义',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='郭德纲相声选',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='金瓶梅',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='西厢记',
        publicate_date='1937-6-15'
    )
    models.Book.objects.create(
        title='聊斋志异',
        publicate_date='1937-6-15'
    )
    return HttpResponse(
        '<script>alert("都是文化人");</script>'
    )


def add_publisher(request):
    # way1
    models.Publisher.objects.create(
        name='人民教育出版社',
        address="欧滴老嘎走私这个疼",
        city='北京',
        country='中国',
        website='www.yinmin.com'
    )
    models.Publisher.objects.create(
        name='山东出版社',
        address='泉城广场地下一层左侧厕所',
        city='山东',
        country='中国',
        website='www.shandong.com'
    )
    return HttpResponse(
        '<script>alert("增加成功");</script>'
    )


def query(request):
    authors = models.Author.objects.all()
    print('all查询：', authors.query)
    for au in authors:
        print(au.id)
        print(au.name)
        print(au.email)
    authors_values = models.Author.objects.values()
    print('value查询：', authors_values)
    for au in authors_values:
        print(au['id'])
        print(au['name'])
        print(au['email'])
    authors_all_values = models.Author.objects.all().values('id', 'name')
    print('value(字段)查询：', authors_all_values)
    for au in authors_all_values:
        print(au['id'])
        print(au['name'])
    authors_values_list = models.Author.objects.values_list('id', 'name')
    print('value_list查询：', authors_values_list)
    for au in authors_values_list:
        print(au[0])
        print(au[1])
    return HttpResponse(
        '<script>alert("查询数据成功")</script>'
    )


def queryall(request):
    author_all = models.Author.objects.all().values()
    a = {"a": author_all}
    return render(request, '03-queryall.html', locals())


def filter_views(request):
    # 查询id为1的author的信息
    ls = models.Author.objects.all()
    print(ls)
    print(ls.filter(id=2, name='王通'))
    print(ls.values('name'))
    print(ls.query)
    return HttpResponse("query ok")


def filed_lookup(request):
    authors = models.Author.objects.all()
    print(authors)
    print(authors.filter(age__gt=20).values())
    print(authors.filter(name__startswith='王').values())
    print(authors.filter(email__contains='qu').values())
    print(authors.filter(
        age__gt=authors
        .filter(name='王通').values('age'))
        .values('name', 'age'))
    return HttpResponse('success')


def exclud(request):
    authors = models.Author.objects.exclude(age__gte=20)
    print(authors.values('name', 'age')[0]['name'])
    return HttpResponse('success')


def update(request, id):
    author = models.Author.objects.get(id=id)
    return render(request, '05-update.html', locals())