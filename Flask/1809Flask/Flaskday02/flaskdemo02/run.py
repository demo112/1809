from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/01-selftemp")
def selftemp():
    html = "<!doctype html>"
    html += "<html>"
    html += "<head>"
    html += "<title>"
    html += "我自己的模版"
    html += "</title>"
    html += "</head>"
    html += "<body>"
    html += "<h1 color=red>"
    html += "这是我第一个模版"
    html += "</h1>"
    html += "</body>"
    html += "</html>"

    return html


@app.route("/02-temp")
def template_views():
    # html = render_template('index.html')
    html = render_template(
        '02-temp.html',
        name="wangwc",
        age=35,
        gender="male")
    return html


@app.route("/03-temp")
def template_views2():
    html = render_template('03-temp.html', name1='歌名：《绿光》', name2='作词：宝强', name3='作词：奶亮', name4='演唱：羽凡')
    return html


@app.route("/04-temp")
def template_views3():
    name1 = '歌名：《绿光》'
    name2 = '作词：宝强'
    name3 = '作词：奶亮'
    name4 = '演唱：羽凡'
    html = render_template('04-temp.html', params=locals())
    return html


@app.route("/04-var")
def var():
    pass
    uname = '他爸爸'
    delay = 880
    lis = ['阿珂', '兰陵王', ' 孙悟空']
    tup = ('阿珂', '兰陵王', ' 孙悟空')
    dic = {
        'AK': '阿珂', 'LLW': '兰陵王', 'WZJ': ' 孙悟空'
    }
    game = Game()
    print(locals())
    return render_template('04-var.html', params=locals())


@app.route("/05-filter")
def filter():
    ustr = "this is a test string"
    return render_template("05-filter.html", params=locals())


@app.route("/06-macro")
def marco():
    # lis = ["孙悟空", "西门庆", "刘姥姥", "小乔"]
    return render_template("05-macro.html")

@app.route("/image")
def image():
    return render_template("image.html")


class Game(object):
    group = '深渊'

    def prt(self):
        return "测试内容" + self.group


if __name__ == "__main__":
    app.run(debug=True)
