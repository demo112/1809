from django.db.models import Avg, Sum, Count, Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def addbook_views(request):
    #方式1 : Entry.objects.create()
    # book=Book.objects.create(title="Python编程基础",publicate_date='2015-10-12')
    # print("新增加的书籍的ID为:%d" % book.id)

    #方式2 : 通过Entry创建对象,对象.save()
    # book = Book(title='数据库基础')
    # book.publicate_date = '2018-01-15'
    # book.save()
    # print("新增加的书籍的ID为:%d" % book.id)

    # Book.objects.create(title='WEB开发基础',publicate_date='2018-01-15')
    # Book.objects.create(title='人工智能的发展',publicate_date='2015-10-12')
    # Book.objects.create(title='数据库的高级进阶',publicate_date='2015-10-12')
    # Book.objects.create(title='Python网络编程',publicate_date='2017-06-30')

    Author.objects.create(name='Wangwc',age=38,email='wangwc@163.com')
    Author.objects.create(name='Rapwang', age=35, email='rapwang@163.com')
    Author.objects.create(name='weimz', age=18, email='weimz@163.com')
    Author.objects.create(name='lvze', age=36, email='lvze@163.com')

    return HttpResponse('Add Book Success')

def query_views(request):
    #1.基本查询操作 - all()
    # books = Book.objects.all()
    # print(type(books))
    # print(books)
    # for book in books:
    #     print('ID:%d,书名:%s,出版日期:%s' % (book.id,book.title,book.publicate_date))
    # print(books.query)#打印输出SQL语句


    #2.查询返回部分列 - values()
    # books = Book.objects.values('title','publicate_date')
    # for book in books:
    #     print("书名:%s,出版日期:%s" % (book['title'],book['publicate_date']))

    #3.查询只返回一条数据 - get()
    # book = Book.objects.get(id=8)
    # print(book.title)

    #4.查询id为1的Book的信息
    # list = Book.objects.filter(id=1)
    # print(list)

    #5.查询publicate_date为2015-10-12的Book的信息
    # list = Book.objects.filter(publicate_date='2015-10-12')

    #6.查询 id为1并且publicate_date为2015-10-12的Book 的信息
    # list = Book.objects.filter(id=1,publicate_date='2015-10-12')
    # for book in list:
    #     print("ID:%d,书名:%s,出版日期:%s" % (book.id,book.title,book.publicate_date))

    #7.查询publicate_date是2015年的所有的数据
    # list = Book.objects.filter(publicate_date__year__gt=2015)
    # for book in list:
    #  print("ID:%d,书名:%s,出版日期:%s" % (book.id,book.title,book.publicate_date))

    # 8.查询Author表中age大于等于30的Author的信息
    list = Author.objects.filter(age__gt=30)
    # 9.查询Author表中所有姓“Wang”的Author的信息
    list = Author.objects.filter(name__startswith='Wang')
    # 10.查询Author表中Email中包含"wang"的Author的信息
    list = Author.objects.filter(email__contains='wang')
    # 11.查询Author表中age大于"RapWang"的age的所有的信息
    list = Author.objects.filter(age__gt=(Author.objects.get(name='Rapwang').age))

    #12.查询Author中年龄不大于35的人的信息
    list = Author.objects.exclude(age__gt=35)
    # for au in list:
    #     print('ID:%d,姓名:%s,年龄:%d,邮箱:%s' % (au.id,au.name,au.age,au.email))
    #13.查询Author表中所有人的平均年龄 - 聚合函数 aggregate()
    # result = Author.objects.aggregate(avg=Sum('age'))
    # print("总年龄为:%d" % result['avg'])
    #14.查询Book表中每个publicate_date所发行的书籍的数量
    list = Book.objects.values('publicate_date').annotate(count=Count('title')).values('publicate_date','count').all()

    list = Book.objects.filter(id__gt=1).values('publicate_date').annotate(count=Count('title')).filter(count__gt=3).values('publicate_date','count').all()
    print(list)
    # for book in list:
    #     print(book['publicate_date'])

    return HttpResponse("<script>alert('查询成功!')</script>")

def authors_views(request):
    authors = Author.objects.filter(isActive=True)
    return render(request,'03-authors.html',locals())

def update_views(request):
    # author = Author.objects.get(id=1)
    # author.age = 40
    # author.save()

    authors=Author.objects.exclude(id=1)
    authors.update(age=45)

    return HttpResponse("Update Success")

def delete_views(request,id):
    # author = Author.objects.get(id=id)
    # author.isActive = False
    # author.save()

    list = Author.objects.filter(id=id)
    list.update(isActive=False)

    return redirect('/03-authors')
    # return HttpResponseRedirect()

def doQ_views(request):
    #获取 id=1 或者 isActive=True的Author们的信息
    authors = Author.objects.filter(Q(id=1)|Q(isActive=True))
    for au in authors:
        print("ID:%d,Name:%s" % (au.id,au.name))
    return HttpResponse('查询成功!')

def oto_views(request):
    #声明 wife 对象,并指定其author信息
    # wife = Wife()
    # wife.name = "伟超夫人"
    # wife.age = 30
    # wife.author_id = 1
    # wife.save()

    # wife = Wife()
    # wife.name = "Rap Girl"
    # wife.age = 19
    # author=Author.objects.get(id=2)
    # wife.author = author
    # wife.save()

    #查询 - 正向查询(通过wife查找author)
    # wife = Wife.objects.get(id=1)
    # author = wife.author
    #

    #查询 - 反向查询(通过author查找wife)
    author=Author.objects.get(id=1)
    wife = author.wife
    print("Wife:%s,Author:%s" % (wife.name,author.name))

    return HttpResponse('OtO OK')






