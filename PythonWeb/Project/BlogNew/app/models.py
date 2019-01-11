"""编写所有的实体类"""
from . import db


class Blogtype(db.Model):
    """博客类型"""
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)
    topics = db.relationship(
        'Topic',
        backref='blogtype',
        lazy = 'dynamic'
    )


class Category(db.Model):
    """博客种类"""
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)
    topics = db.relationship(
        'Topic',
        backref='category',
        lazy = 'dynamic'
    )


class Reply(db.Model):
    """回复"""
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    reply_time = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)


class Topic(db.Model):
    """帖子"""
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)
    read_num = db.Column(db.Integer, default=0, nullable=True)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text, nullable=True)
    blogtype_id = db.Column(db.Integer, db.ForeignKey('blogtype.id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=True)
    replies = db.relationship(
        'Reply',
        backref='topic',
        lazy = 'dynamic'
    )


class User(db.Model):
    """用户"""
    __tablename__ = 'user'
    ID = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(50), nullable=True)
    upwd = db.Column(db.String(50), nullable=False)
    is_author = db.Column(db.Boolean, default=False)
    topics = db.relationship(
        'Topic',
        backref='user',
        lazy = 'dynamic'
    )
    replies = db.relationship(
        'Reply',
        backref='user',
        lazy = 'dynamic'
    )

    vokes_topics = db.relationship(
        'Topic',
        secondary='voke',
        backref=db.backref('voke_users',lazy='dynamic'),
        lazy='dynamic'
    )


class Voke(db.Model):
    """点赞"""
    __tablename__ = 'voke'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
