from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/day06'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    uemail = db.Column(db.String(200))

    def __repr__(self):
        return "<User:%r>" % self.uname


@app.route('/add')
def add_to():
    users = Users()
    users.uname = 'wang3'
    users.uage = 19
    users.uemail = 'wang114@163.com'
    db.session.add(users)
    return "添加成功"


@app.route('/check')
def check_views():
    print(db.session.query(Users).all())
    return "checked Success"


@app.route('/table', methods=['GET', "POST"])
def table_views():
    users = db.session.query(Users).all()
    if request.method == "GET":
        return render_template('table.html', users=users)
    # else:
    #     return change_views(users)


@app.route('/adduser', methods=['GET', "POST"])
def add_views():
    if request.method == "GET":
        return render_template('adduser.html')
    else:
        users = Users()
        users.uname = request.form.get('uname')
        users.uage = request.form.get('uage')
        users.uemail = request.form.get('uemail')
        db.session.add(users)
        return table_views()


@app.route('/update', methods=['GET', "POST"])
def change_views():
    if request.method == "GET":
        index = request.args.get('id')
        users = db.session.query(Users).all()
        user = db.session.query(Users).filter_by(id=index).first()
        print(user, index)
        return render_template('table_change.html', user=user, users=users)
    else:
        return 'POST'


if __name__ == "__main__":
    manager.run()
