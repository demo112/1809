from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bgfasdfsdfsvbewioranhgviowegobirvwnilbuesrh'


@app.route('/01-addsession')
def addsession():
    session['uname'] = "admin"
    session['upsw'] = 'admin'
    return "向session中添加数据成功"


@app.route('/02-getsession')
def getsession():
    if 'uname' in session and "upsw" in session:
        uname = session['uname']
        upsw = session['upsw']
        print(uname, upsw)
        return "获取session数据成功"
    else:
        return "session中没有数据"


if __name__ == '__main__':
    app.run(debug=True)
