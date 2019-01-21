# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import *
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
    author_all = models.Author.objects.filter(isActive=True).all().values()
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


def update(request, auid):
    author = models.Author.objects.filter(isActive=True).get(id=auid)
    return render(request, '05-update.html', locals())


def aggregate(request):
    # 查询所有人的年龄总和
    result = models.Author.objects.aggregate(sumAge=Sum('age'), min=Min('age'), max=Max('age'))
    print('查询所有人的年龄总和,最大，最小：', result)
    # 查询所有人的平均年龄
    average = models.Author.objects.aggregate(avgAge=Avg('age'))
    print('查询所有人的平均年龄：', average)
    # 年龄大于20的人数
    count = models.Author.objects.filter(age__gt=20).aggregate(num=Count('age'))
    print('年龄大于20的人数：', count)
    return HttpResponse('聚合查询成功')


def annotate(request):
    result = models.Author.objects.values('isActive').annotate(num=Count('*'))
    print(result)
    return HttpResponse("分组聚合成功")


def annotate_book(request):
    # 总数
    result = models.Book.objects.aggregate(count=Count('isActive'))
    print(result)
    # 每段时间发布书籍数量
    result11 = models.Book.objects.values('isActive').annotate(count=Count('*'))
    print(result11)
    result12 = models.Book.objects.values('isActive').annotate(count=Count('*')).values('count')
    print(result12)
    result13 = models.Book.objects.values('isActive').annotate(count=Count('*')).values("count")[0]
    print(result13)
    result14 = models.Book.objects.values('isActive').annotate(count=Count('*')).values("count")[0]['count']
    print(result14)
    # 1936年后的数量
    result2 = models.Book.objects.\
        filter(publicate_date__year__gte=1936).\
        values('publicate_date').\
        annotate(count=Count('*'))
    print(result2)
    # 1936年后的数量
    # todo
    result3 = models.Publisher.objects.filter(city="北京").annotate(count=Count('*')).values()
    print('111', result3)
    return HttpResponse("练习分组/聚合成功")


def update08(request):
    # 获取王通的值
    # author = models.Author.objects.get(name='王通')
    # # 修改email
    # author.email = "wanglegetong@163.com"
    # # 保存其会数据库
    # author.save()
    author = models.Author.objects.all().update(isActive=True)
    print(author)

    # models.Author.objects.all().update(age=F('age') + 10)
    author_or = models.Author.objects.filter(Q(id=1) | Q(isActive=True))
    print(author_or)
    return HttpResponse('修改信息成功')


def delete(request, auid):
    author = models.Author.objects.all().get(id=auid)
    author.isActive = False
    author.save()
    print(1)
    return redirect('/03-queryall')


def oto_views(request):
    """一对一绑定"""
    wife = models.Wife()
    wife.name = "屈夫人"
    wife.age = 18

    # 方式一：通过id关联
    wife.author_id = 1

    # 方式二：通过作者关联
    wife.author = models.Author.objects.get(name="屈亚伟")
    wife.save()
    return HttpResponse('找老婆成功')


def oto_find(request):
    """一对一查询"""
    wife = models.Author.objects.get(name="王通").wife
    print(wife)
    author = models.Author.objects.get(id=wife.author_id)
    print(author)
    return HttpResponse('找老婆成功')


def onetomany(request):
    """一对多添加数据"""
    # 方法一
    book = models.Book.objects.get(title="三国演义")
    book.publisher_id = 2
    book.save()
    # 方法2
    book2 = models.Book.objects.get(title="射雕英雄传")
    book2.publisher = models.Publisher.objects.get(id=5)
    book2.save()
    return HttpResponse('一对多成功')


def find_otm(request):
    """查询一对多"""
    # 正向查询
    book = models.Book.objects.get(id=1)
    publisher = book.publisher
    # 反向查询
    books = publisher.book_set.all().values()
    print(books)
    return render(request, "11-otm.html", locals())


def add_mtm(request):
    au1 = models.Author.objects.get(id=1)
    au2 = models.Author.objects.get(id=2)
    au3 = models.Author.objects.get(id=3)
    book = models.Book.objects.get(title="射雕英雄传")
    book.author_set.add(au1, au2, au3)
    book.author_set.remove(au1)
    au = book.author_set.popitem(au2)
    print(au)
    book.author_set.clear()

    return HttpResponse('添加多对多成功')

def find_mtm(request):
    # 正向查询
    book = models.Book.objects.get(title='碧血剑')
    authors = book.author_set.all()
    # 反向查询
    au = models.Author.objects.get(name="王通")
    books = au.book_set.all()
    return render(request, '12-mtm.html', locals())


def object_views(request):
    count = models.Author.objects.age_count(25)
    return HttpResponse("年龄大于等于20岁的人共有:%d" % count)


def name_like_views(request):
    count = models.Author.objects.name_like("王")
    return HttpResponse(count)


def book_date_views(request):
    info = models.Book.objects.book_date('1937')
    return HttpResponse(info)
