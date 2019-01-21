from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_protect

from index.form import *
from index.models import Users


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