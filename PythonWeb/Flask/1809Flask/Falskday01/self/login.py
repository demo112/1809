from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "This is my first flask demo"


@app.route('/login')
def login():
    return '<h1>欢迎来到登陆页面</h1>'


@app.route('/register')
def register():
    return "欢迎来到注册页面"


@app.route('/calc/<int:a>/<int:b>')
def add(a, b):
    c = str(a + b)
    return c


@app.route("/show/<name>")
def show(name):
    return name


@app.route('/show/<name>/<int:age>')
def age(name, age):
    """# 带多个参数使用/隔开，并继续用<>来表示"""
    return name + " 年龄 " + age


@app.route("/")
@app.route("/index")
@app.route('/<int:number>')
@app.route("/index/<int:number>")
def index_views(number=1):
    # return '您输入的页数是' + str(number)
    return '您输入的页数是:%d' % number


@app.route('/post', methods=["POST","GET"])
def post():
    return "该方法允许接受GET和POST请求"


if __name__ == "__main__":
    app.run(debug=True)
