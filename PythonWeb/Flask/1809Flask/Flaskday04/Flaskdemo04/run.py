import os
import random
import datetime

from flask import Flask, request, render_template
import sqlalchemy
app = Flask(__name__)


@app.route('/01-file', methods=['GET', "POST"])
def file_views():
    if request.method == "GET":
        return render_template('01-file.html')
    else:
        uname = request.form.get('uname')
        print("用户名" + uname)
        f = request.files['uimg']
        print("用户名" + f.filename)
        # 获取项目绝对路径
        basedir = os.path.dirname(__file__)
        print(basedir)
        # 避免文件名重复
        # 获取文件拓展名
        ext = f.filename.split(".")[1]
        # 获取时间
        ftime = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        # 获取随机数
        fran = str(random.randrange(0, 9999999, 1))
        filename = ftime + fran + '.' + ext
        # 保存成存储的路径
        upload = os.path.join(basedir, 'static//upload', filename)

        f.save(upload)
        return '获取成功'


if __name__ == "__main__":
    app.run(debug=True)
