from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    """首页"""
    return HttpResponse("这里是music下的index返回值")


def template_loader(request):
    """加载模版文件"""
    t = loader.get_template("01-templates.html")
    html = t.render()
    print("loader方法")
    return HttpResponse(html)


def template1_render(request):
    """加载模版文件"""
    print('render方法')
    return render(request, '01-templates.html')


def template_var(request):
    """有参数模版文件"""
    class Person(object):
        uname = None

        def intro(self):
            return "hello, my name is %s" % self.uname

    person = Person()
    person.uname = "吕"

    uname = 'wang'
    uage = "18"
    ls = ['a', 'b', 'c']
    dic = {
        'swk': '孙悟空',
        'ZWN': '猪悟能'
    }
    return render(request, '02-var.html', locals())


def template_static(request):
    """展示调用static资源"""
    return render(request, '03-static.html')
