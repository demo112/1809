from flask import Flask

#将当前运行的主程序构建成Flask应用,以便接收用户的请求(request)和响应(response)
app = Flask(__name__)

#@app.route('/') : 定义Flask中的路由,主要定义用户的访问路径. '/'表示的是整个网站的根路径
#def index() : 表示的是匹配上@app.route()的路径后的处理程序-视图处理函数(Views),所有的视图处理函数必须要有一个return,必须要return一个字符串


@app.route('/')
def index():
    return "My First Flask Demo"


@app.route('/login')
def login():
    return "欢迎访问登录页面"


@app.route('/register')
def register():
    return "欢迎访问注册页面"

#定义带参数的路由以及视图处理函数
@app.route('/show/<name>')
def show1(name):
    return "<h1>传递进来的参数为:%s</h1>" % name

#路径: localhost:5000/show/wangwc/25
@app.route('/show/<name>/<int:age>')
def show2(name,age):
    # age = int(age)
    return "姓名:%s,年龄:%d" % (name,age)

if __name__ == "__main__":
    #运行Flask应用(启动Flask服务),默认会在本机开启5000端口,允许使用 http://localhost:5000/ 访问 Flask的web应用
    #debug=True,将运行模式更改为调试模式(开发环境中推荐使用True,生产环境中必须改为False)
    app.run(debug=True)