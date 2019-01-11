"""处理main业务中的路由和视图处理函数"""
import datetime

from flask import render_template, request, session, redirect
import os

from . import main
from .. import models, db


@main.route('/')
@main.route('/index')
def main_index():
    """主页"""
    if "loginname" in session:
        loginname = session['loginname']
        user = models.User.query.filter_by(loginname=loginname).first()
        uname = user.uname
    # 查询category中的所有数据
    categories = models.Category.query.all()
    topics = models.Topic.query.all()
    return render_template('index.html', params=locals())


@main.route('/list')
def list_catepory():
    """选项列表"""
    cid = request.args['id']
    return cid


@main.route('/login', methods=['GET', "POST"])
def login():
    """登陆逻辑"""
    if request.method == "GET":
        if 'loginname' in session:
            return redirect('/')
        url = request.headers.get('Referer', '/')
        session['url'] = url
        return render_template('login.html')
    else:
        loginname = request.form['username']
        password = request.form['password']
        user = models.User.query.filter_by(loginname=loginname, upwd=password).first()
        if user:
            session['id'] = user.ID
            session['loginname'] = loginname
            return redirect('/')
        else:
            return redirect('/login')


@main.route('/logout', methods=['GET', "POST"])
def logout():
    """退出登陆"""
    loginname = session['loginname']
    use = models.User.query.filter_by(loginname=loginname).first()

    del session['loginname']
    del session['id']
    url = request.headers.get('Referer', '/')
    if use.is_author:
        return redirect('/')
    return redirect(url)


@main.route('/release', methods=['GET', "POST"])
def release():
    """
        判断是否是作者
        决定是否打开发表界面
        并将发表内容提交数据库
    """
    if request.method == "GET":
        url = request.headers.get('Referer', '/')
        if 'loginname' in session:
            loginname = session['loginname']
            categories = models.Category.query.all()
            user = models.User.query.filter_by(loginname=loginname).first()
            uname = user.uname
            if user.is_author:
                categories = models.Category.query.all()
                return render_template('release.html', params=locals())
        return redirect(url)
    else:
        # post请求处理发表博客的相关操作
        # 创建topic的对象
        topic = models.Topic()
        # 接受前段传递的值并复制给topic
        # 接受title
        topic.title = request.form['author']
        # 接受blogtype_id
        topic.blogtype_id = request.form['list']
        # 接受category_id
        topic.category_id = request.form['category']
        # 从session中得到用户的id
        topic.user_id = session['id']
        # 接受传递过来的content
        topic.content = request.form['content']
        # 接受时间，获取系统当前时间给pub_date
        topic.pub_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(
            "标题：%s, 类型： %s，内容类型：%s, 用户：%s，内容：%s，时间：%s" %
            (topic.title, topic.blogtype_id, topic.category_id,
             topic.user_id, topic.content, topic.pub_date))
        # # 判断是否有文件上传，有的话保存至static/upload并将路径上传数据库
        if request.files:
            # 获取需要上传的文件
            f = request.files['picture']
            # 处理文件名
            f_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            ext = f.filename.split('.')[1]
            filename = f_time + '.' + ext
            # 处理上传路径
            topic.images = 'upload/' + filename
            # 将文件以新文件名的形式保存在指定路径下
            basedir = os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir, "static/upload", filename)
            f.save(upload_path)
        # 将topic对象保存回数据库
        db.session.add(topic)
        print(topic)
        return redirect('/')


@main.route('/info')
def info():
    """博客详情页"""
    if "loginname" in session:
        loginname = session['loginname']
        user = models.User.query.filter_by(loginname=loginname).first()
        uname = user.uname
    # 查询category中的所有数据
    categories = models.Category.query.all()
    topics = models.Topic.query.all()
    topic_id = request.args['id']
    # 获取博客
    if models.Topic.query.filter_by(id=topic_id).first():
        topic = models.Topic.query.filter_by(id=topic_id).first()
        topic_before = db.session.query(models.Topic).filter(models.Topic.id < topic_id).order_by('id desc').first()
        topic_after = db.session.query(models.Topic).filter(models.Topic.id > topic_id).first()
        # 获取阅读量并加一保存
        read_num = int(topic.read_num) + 1
        topic.read_num = read_num
        db.session.add(topic)
        db.session.commit()
        return render_template('info.html', params=locals())
    else:
        return "你想看啥"
