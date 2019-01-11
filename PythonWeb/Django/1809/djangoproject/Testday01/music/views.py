from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def show(request):
    return "这是music应用中的show访问的路径"
