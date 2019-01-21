from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from index.models import *


def index(request):
    """主页"""
    # todo sessison处理
    # if "loginname" in session:
    #     loginname = session['loginname']
    #     user = models.Users.query.filter_by(loginname=loginname).first()
    #     uname = user.uname
    # 查询category中的所有数据
    # categories = models.Category.query.all()
    # topics = models.Topic.query.all()
    # return render(request, 'index.html', locals())
    return HttpResponse('<h1>假的主页</h1>')
