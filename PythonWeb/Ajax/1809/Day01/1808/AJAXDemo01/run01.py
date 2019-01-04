from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/01-xhr')
def xhr():
    return render_template('01-xhr.html')

@app.route('/server')
def server():
    uname = request.args.get('uname')
    #return "我的第一个AJAX请求"
    return "参数值为:"+uname

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')