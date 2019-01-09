import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/01-server')
def server():
    return 'Hello World!'


@app.route('/02-server')
def cross_server():
    # 由前端决定处理函数
    part = request.args['callback']
    # return 'console.log("这是02-server动态返回的数据");'
    # 指定前端的那个方法来执行服务器端响应的内容
    # return 'cross_server("这是02-server动态返回的数据")'
    dic = {
        'uname': 'na',
        'uage': 16,
        'ugender': 'male'
    }
    json_dic = json.dumps(dic)
    return part + "(" + json_dic + ");"

@app.route('/03-flight')
def flight():
    """跨域练习：显示航班信息"""
    print('1111')
    callback = request.args['callback']
    print(callback)
    dic = {
        'flightNO': 'MM233',
        'from': 'beijing',
        'to': 'shanghai',
        'date': '17:05'
    }
    return callback + "(" + json.dumps(dic) + ")"
    # ask http://localhost:5000/static/03-flight.html

    # show flight info of flight plan when click button
    # send a request to http://127.0.0.1:5000/03-fight
    # and get response

    # show response msg :
    # fightNO:MM233
    # start: beijing
    # to: shanghai
    # date: 17:05
    pass


if __name__ == '__main__':
    app.run(debug=True)
