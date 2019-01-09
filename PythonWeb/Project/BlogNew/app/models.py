# 编写所有的实体类
from . import db


class Blogtype(db.Model):
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)
    topics = db.relationship(
        'Topic',
        backref='blogtype',
        lazy = 'dynamic'
    )

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)
    topics = db.relationship(
        'Topic',
        backref='category',
        lazy = 'dynamic'
    )

class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    content = db.Column(db.Text, nullable=False)
    reply_time = db.Column(db.DateTime, nullable=True)


class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)
    read_num = db.Column(db.Integer, nullable=True)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text, nullable=True)
    blogtype_id = db.Column(db.Integer, db.ForeignKey('blogtype.id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=True)
    replys = db.relationship(
        'Reply',
        backref='topic',
        lazy = 'dynamic'
    )
    vokes = db.relationship(
        'Voke',
        backref='topic',
        lazy = 'dynamic'
    )


class User(db.Model):
    __tablename__ = 'user'
    ID = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(50), nullable=True)
    upwd = db.Column(db.String(50), nullable=False)
    is_author = db.Column(db.Boolean(4), default=False)
    replys = db.relationship(
        'Reply',
        backref='user',
        lazy = 'dynamic'
    )
    topics = db.relationship(
        'Topic',
        backref='user',
        lazy = 'dynamic'
    )
    vokes = db.relationship(
        'Voke',
        backref='user',
        lazy = 'dynamic'
    )


class Voke(db.Model):
    __tablename__ = 'voke'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)