from flask import Flask

# 构造flask的一个对象，将当前运行的flask主程序构建成Flask应用，
# 以便接收用户的请求（request）并给出相应（response）
app = Flask(__name__)


# @app.route('/') : 定义Flask中的路由,主要定义用户的访问路径. '/'表示的是整个网站的根路径
# def index() : 表示的是匹配上@app.route()的路径后的处理程序-视图处理函数(Views),所有的视图处理函数必须要有一个return,所以必须要return内容（比如一个字符串）
@app.route("/")
def index():
    return "This is my first flask demo"


if __name__ == "__main__":
    # 运行Flask应用(启动Flask服务),默认会在本机开启5000端口,允许使用 http://localhost:5000/ 访问 Flask的web应用
    # debug=True,将运行模式更改为调试模式(开发环境中推荐使用True（代码的更改可以及时被识别出来）,生产环境中必须改为False（代码的更改必须重启服务才能应用）)
    app.run(debug=True)

# 解决问题端口占用：
#   way1
#   app.run(debug=True，port=新端口号)
#   way2
#   杀死进程
#   netstat -lptu
#   sudo kill -9 PID
