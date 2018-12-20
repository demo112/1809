from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/<int:num>')
@app.route('/index/<int:num>')
def index(num=None):
    if num is None:
        num = 1
    return "您想看的页数为:%d" % num


@app.route('/method',methods=['POST','GET'])
def method():
    return "这是使用POST/GET请求提交过来的"


@app.route('/admin/login/form/show')
def show():
    return "这是admin路径下的login路径下的form的路径下的show"


@app.route('/admin/login/form/show/<name>/<age>')
def show1(name,age):
    return "参数name的值为:%s,参数age的值为:%s" % (name,age)

@app.route('/url')
def url():
    url = url_for('show1',name='wangwc',age=35)
    print('反向生成的地址为:'+url)
    return "<a href='%s'>跳转至show1</a>" % url

    # url=url_for('show')
        # print('反向生成的地址为:'+url)
        # return "<a href='%s'>去往show</a>" % url
        # return "<a href='/admin/login/form/show'>去往show</a>"

if __name__ == "__main__":
    # app.run(debug=True,port=5555,host='0.0.0.0')
    app.run(debug=True,host='0.0.0.0')