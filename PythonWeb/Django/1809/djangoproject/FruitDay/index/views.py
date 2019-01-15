from django.shortcuts import render


# Create your views here.
def index(request):
    """主页"""
    return render(request, 'index.html')


def signin(request):
    """注册"""
    return render(request, 'signin.html')


def signup(request):
    """登陆"""
    return render(request, 'signup.html')
