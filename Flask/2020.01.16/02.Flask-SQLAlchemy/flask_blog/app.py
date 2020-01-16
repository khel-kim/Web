# 나중에 post에 들어갈 시간을 입력하기 위해
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.config["SECRET_KEY"] = 'this is secret'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

# SQLALCHEMY_TRACK_MODIFICATIONS은 추가적인 메모리를 필요로 하므로 꺼두자.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')

    # 관계 설정
    posts = db.relationship('Post', backref='author', lazy=True)
    # db.relationship(class name, backref=Post가 backref를 할 때 필드 이름, lazy=??)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email

        # 비밀 번호 hash화
        self.set_password(password)

    def __repr__(self):
        return f"User: '{self.id}', '{self.username}', '{self.email}'"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    __table_name__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post: '{self.id}', '{self.title}'"


@app.route('/')
@app.route('/index/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run()
