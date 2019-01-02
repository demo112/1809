from flask import Flask, render_template

app = Flask(__name__)

@app.route('/01-var')
def var_views():
    name = '隔壁老王'
    age = 32
    salary = 125.55
    tup = ('老魏','老王','老吕','小蒙蒙')
    list = ['漩涡鸣人','宇智波佐助','春野樱']
    dic = {
        'C':'CHINA',
        'A':'AMERICA',
        'J':'JAPAN',
    }
    dog = Dog()
    return render_template('01-var.html',params=locals())


@app.route('/02-filter')
def filter_views():
    title = 'this is my FIRST filter page'
    return render_template('02-filter.html',title=title)

@app.route('/03-if')
def if_views():
    return render_template('03-if.html',age=25,uname='超哥哥')


@app.route('/04-for')
def for_views():
    list = ["武大郎","潘金莲","王宝强","王伟超"]
    dic = {
        "SWK":'孙悟空',
        "ZWN":'猪八戒',
        "SWJ":'沙悟净',
        "WWC":'王伟超',
        "TSZ":'唐三藏',
    }
    return render_template('04-for.html',params=locals())


@app.route('/05-macro')
def macro_views():
    list = ["王老师","隔壁老王","WANGWC","王伟超老师","RapWang","超哥哥"]
    return render_template('/05-macro.html',params = locals())

@app.route('/06-static')
def static_views():
    return render_template('06-static.html')

class Dog(object):
    name = "旺财"
    def eat(self):
        return self.name + "吃狗粮"

if __name__ == "__main__":
    app.run(debug=True)