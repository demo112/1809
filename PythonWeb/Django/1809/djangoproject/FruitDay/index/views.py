from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from werkzeug.security import generate_password_hash, check_password_hash


from index import models


def index(request):
    """主页"""

    return render(request, 'index.html')


def login(request):
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
            id = request.COOKIES['id']
            uphone = request.COOKIES['uphone']
            user = models.Users.objects.filter(id=id, uphone=uphone)
            if user:
                request.session['id'] = id
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
