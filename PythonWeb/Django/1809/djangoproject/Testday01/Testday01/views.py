from django.http import HttpResponse


def show(request):
    """django视图处理函数中必须有一个参数，名称必须叫request"""
    return HttpResponse("我的第一个Django程序")


def show01(request):
    """django视图处理函数中必须有一个参数，名称必须叫request"""
    return HttpResponse("我的show01 Django程序")


def show02(request, year):
    """http://lcoalhost:8000/show/2017"""
    return HttpResponse("参数为" + year)


def show03(request, year, month, day):
    """http://lcoalhost:8000/show/2017"""
    return HttpResponse("生日为" + year + '年' + month + "月" + day + '日')
