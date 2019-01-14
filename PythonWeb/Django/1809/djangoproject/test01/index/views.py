from django.http import HttpResponse
# Create your views here.


def index(request):
    """
        方法一：通过主应用的urls直接调用首页
        方法二：通过轮空调用到index.urls调用该视图函数
    """
    return HttpResponse("这里是index下的index返回值")


def register(request):
    """
        方法一：通过主应用的urls直接调用注册
        方法二：通过轮空调用到index.urls调用该视图函数
    """
    return HttpResponse('这是index中deregister访问路径')


def login(request):
    """
        方法一：通过主应用的urls直接调用注册
        方法二：通过轮空调用到index.urls调用该视图函数
    """
    return HttpResponse('这是index中login访问路径')
