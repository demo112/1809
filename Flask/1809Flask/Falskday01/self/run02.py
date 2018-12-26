from flask import Flask, url_for

app = Flask(__name__)


@app.route("/index")
def index():
    return '这是首页'

@app.route("/url")
def url():
    # '通过index的函数名。反向生成对应的请求地址'
    url_index = url_for('index')
    print(url_index)
    return "<a href='%s'>返回首页</a>" % url_index


# 通过复杂的地址，简单方法名称，加参数
@app.route('/admin/login/form/url/show/<name>')
def show(name):
    return "传递进来的参数是" + name


@app.route('/url_')
def url_parameter():
    url_show = url_for('show',name="wangwc")
    print(url_show)
    return '<a href="%s">访问show</a>' % url_show


if __name__ == "__main__":
    app.run(debug=True)
