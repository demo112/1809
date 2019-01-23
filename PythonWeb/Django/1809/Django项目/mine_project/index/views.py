#!/usr/bin/python
# -*- coding:utf8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_protect
from werkzeug.security import generate_password_hash

from django.core import serializers
from index.form import *
from index import models
import json


def request_views(request):
    print(dir(request))
    return HttpResponse(
        "<a href='/show_index/'>测试的链接</a>"
    )


def show_index(request):
    scheme = request.scheme
    body = request.body
    path = request.path
    get_full_path = request.get_full_path
    get_host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    if 'HTTP_REFERER' in request.META:
        meta = request.META.get('HTTP_REFERER', '/')
    else:
        meta = "没有请求原地址"
    return render(request, '01-showrequest.html', locals())


# todo 不好使
@csrf_protect
def post_views(request):
    """
    判断请求方式，如果是get就去show_request
    是post就去接受数据
    """
    if request.method == "GET":
        return render(request, '02-post.html')
    else:
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        return HttpResponse("用户名：%s 密码：%s" % (uname, upwd))


def form(request):
    if request.method == "GET":
        form_re = RemarkForm()
        return render(request, '03-form.html', locals())
    else:
        # 通过forms.Form的子类的构造器接收表单数据
        form_re = RemarkForm(request.POST)
        # 2.必须使form通过验证之后再取值
        if form_re.is_valid():
            # 3.获取表单的数据
            cd = form_re.cleaned_data
            print(cd)
            return HttpResponse('取值成功')
        return HttpResponse('取值失败')


def register(request):
    if request.method == "GET":
        # # 使用自定义的form类
        # register = RegisterForm()
        # 使用关联form类
        form_register = ModelRegisterForm()
        return render(request, '04-register.html', locals())
    else:
        # # 使用自定义的form类
        # register = RegisterForm(request.POST)
        # 使用关联form类
        form_register = ModelRegisterForm(request.POST)
        if form_register.is_valid():
            cd = form_register.cleaned_data
            print(cd)
            user = Users.objects.filter(uname=cd['uname'])
            if user:
                return HttpResponse('用户已存在')
            else:
                user = Users(**cd)
                # user.uname = cd['uname']
                # user.upwd = cd['upwd']
                # user.uage = cd['uage']
                # user.uemail = cd['uemail']
                user.save()
            return HttpResponse('注册成功')
        return HttpResponse('请联系张起硕')


def login(request):
    if request.method == "GET":
        form_user = ModelLoginForm()
        return render(request, '05-login.html', locals())
    else:
        form_user = ModelLoginForm(request.POST)
        if form_user.is_valid():
            cd = form_user.cleaned_data
            user = Users.objects.filter(uname=cd['uname'])
            if user and cd['upwd'] == user.values()[0]['upwd']:
                return HttpResponse('登陆成功')
        return HttpResponse('登陆失败')


def widget(request):
    if request.method == "GET":
        widget_form = WidgetForm()
        return render(request, '06-widght.html', locals())


def set_cookie(request):
    resp = HttpResponse("成功响应数据到客户端")
    expires = 60*60*1
    resp.set_cookie("USERID", "6666666", expires)
    return resp


def get_cookie(request):
    if "USERID" in request.COOKIES:
        print("userid的值：", request.COOKIES['USERID'])
    return HttpResponse("获取成功")


def set_session(request):
    request.session['USERID'] = '6666678'
    request.session['UNAME'] = 'lixiao'
    return HttpResponse("session数据保存成功")


def get_session(request):
    print('userid:', request.session['USERID'])
    print('uname:', request.session['UNAME'])
    return HttpResponse("session数据读取成功")


def ajax_get(request):
    return HttpResponse(
        'This is an get request from ajax in Django')


def ajax_params(request):
    # 接受提交的数据
    uname = request.GET['uname']
    upwd = request.GET['upwd']
    # 将处理后的数据返回网页
    return HttpResponse('姓名：%s<br>密码：%s' % (uname, upwd))


def ajax_post(request):
    if request.method == 'GET':
        return render(request, '13-ajax-post.html')
    else:
        uname = request.POST['uname']
        s = "传递过来的是：%s" % uname
    return HttpResponse(s)


def index(request):
    """主页"""
    return render(request, 'index.html')


def login_fruitday(request):
    """登陆"""
    if request.method == "GET":
        url = request.META.get('HTTP_REFERER', '/')
        print('denglu')
        print(url)
        request.session['url'] = url
        # todo 将url加入session中
        if 'uphone' in request.session and 'id' in request.session:
            # 判断session是有存在
            return redirect(url)
        # 继续判断cookie有没有保存密码
        if 'uphone' in request.COOKIES and 'id' in request.COOKIES:
            # 存在，判断正确性
            uid = request.COOKIES['id']
            uphone = request.COOKIES['uphone']
            user = models.Users.objects.filter(id=uid, uphone=uphone)
            if user:
                request.session['id'] = uid
                request.session['uphone'] = uphone
                return redirect(url)
            else:
                # todo 不正确删除cookies
                del request.COOKIES

        return render(request, 'login.html')

        # todo 处理cookies
        # if 'uphone' in request.cookies:
        #     user = models.Users.objects.filter_by(uname=request.cookies['uphone']).first()
        #     if user and check_password_hash(user.upwd, request.cookies['upwd']):
        #         return render_template('index.html')
        # return render_template('signup.html')
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        print(uphone, upwd)
        # 验证用户名即密码是否正确
        user = models.Users.objects.filter(uphone=uphone, upwd=upwd)
        url = request.session['url']
        if user:
            print('登陆成功')
            # todo 处理session
            request.session['id'] = user[0].id
            request.session['uphone'] = uphone
            # 判断是否要存cookie
            # todo 处理cookie
            # todo 从session中获取源地址
            resp = redirect(url)
            if 'remember' in request.POST:
                print('保存密码')
                resp.set_cookie('uphone', uphone, 60 * 60 * 24 * 365 * 20)
                # 此处密码是明文
                resp.set_cookie('id', user[0].id, 60 * 60 * 24 * 365 * 20)
            return resp
        else:
            # 登陆失败
            errmsg = True
            return render(request, 'login.html', locals())


def signup(request):
    """注册"""
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        uphone = request.POST.get("uphone")
        user_in = models.Users.objects.filter(uphone=uphone)
        if user_in:
            return render(request, 'signup.html', {'errMSg': '用户已存在'})
        else:
            user = models.Users()
            user.uphone = uphone
            upwd = request.POST.get("upwd")
            user.upwd = generate_password_hash(upwd)
            user.uemail = request.POST.get("uemail")
            user.uname = request.POST.get("uname")
            try:
                user.save()
                # todo 将user加入session
                request.session['user'] = user
                request.session['uphone'] = uphone
                return redirect('/')
            except Exception as ex:
                print(ex)
            return render(request, 'signup.html', {'errMSG': '请联系管理员'})


def ajax_json(request):
    # ls = [
    #     {
    #         'name': 'wang',
    #         'age': 17,
    #         'gender': 'male'
    #     },
    #     {
    #         'name': 'meng',
    #         'age': 20,
    #         'gender': 'female'
    #     },
    # ]
    # json_str = json.dumps(ls)
    # return HttpResponse(json_str)
    users = models.Users.objects.all()
    # 由于users是不可以被json序列化的，所以无法使用json.dump（）函数
    json_str = serializers.serialize('json', users)
    print(json_str)
    return HttpResponse(json_str)
