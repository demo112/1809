from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """主页"""
    return HttpResponse("这里是sport下的index返回值")
