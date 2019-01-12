from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """主页"""
    return HttpResponse("这里是news下的index返回值")
