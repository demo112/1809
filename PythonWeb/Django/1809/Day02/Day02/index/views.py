from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def login_views(request):
    return HttpResponse("这是index应用中的login访问路径")

def register_views(request):
    return HttpResponse('这是index应用中的register访问路径')

def index_views(request):
    return HttpResponse('这是index应用中的index访问路径')

def temp_views(request):
    #1.通过loader加载模板
    t=loader.get_template('01-temp.html')
    #2.将模板渲染成字符串
    html=t.render()
    #3.将字符串通过HttpResponse响应给客户端
    return HttpResponse(html)

def temp02_views(request):
    return render(request,'01-temp.html')

def var_views(request):
    str = "这是模板中的字符串"
    num = 3306
    tup = ('西游记','水浒传','三国演义','红楼梦')
    list = ['孙悟空','西门庆','曹操','林黛玉']
    dic = {
        'BJ':'北京',
        'SZ':'深圳',
        'SH':'上海',
    }
    dog = Animal()
    ret = sayHi()
    return render(request,'02-var.html',locals())




def sayHi():
    return "Hello,this is a function ..."

class Animal(object):
    name = '王富贵'
    def eat(self):
        return "eat "+self.name


