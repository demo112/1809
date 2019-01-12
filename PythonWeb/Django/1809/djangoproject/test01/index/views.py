from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """首页"""
    return HttpResponse("这里是index下的index返回值")
