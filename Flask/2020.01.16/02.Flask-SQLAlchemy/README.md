# Flask-SQLAlchemy

[TOC]

```
flask_blog/
	templates/
		index.html
	static/
		profile_imgs/
			default.png
    app.py
    site.db
```

목표: 사용자와 게시물에 대한 정보를 저장하기 위한 데이터베이스를 제작

본 프로젝트에서 사용자는 사용자 계정 이름을 갖고, 이메일과 암호가 있으며, 프로필 사진을 저장할 수 있는 공간이 필요하다.

Flask는 데이터베이스 기능을 내장하고 있지 않기 때문에 우리는 적절한 데이터베이스를 골라서 사용해야한다. 각 데이터베이스마다 사용되는 API도 다르고, SQL 문법도 다르지만 ORM(Object Relation Model) 덕분에 코드는 특정 데이터베이스에 종속되지 않고, 기본 객체 만으로 데이터를 기술할 수 있다.

파이썬에서 ORM으로 많이 쓰이는 것 중 SQLAlchemy가 있는데, 이를 Flask에서 플러그인처럼 사용하기 쉽게 만들어진 Flask-SQLAlchemy가 있다.

``` 
$ pip install flask_sqlalchemy
```

`app.py`에 flask_sqlalchemy 임포트 하기

``` python
# app.py

# 나중에 post에 들어갈 시간을 입력하기 위해
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# ...
```

추가로 secret key와 db 위치 설정하고 SQLAlchemy  객체 만들기

```python
# app.py

# ...

app = Flask(__name__)

app.config["SECRET_KEY"] = 'this is secret'
app.config["SQLALCHEMY_DATABASE_URI"] = 'splite://site.db'

# SQLALCHEMY_TRACK_MODIFICATIONS은 추가적인 메모리를 필요로 하므로 꺼두자.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ...
```

## 사용자 모델 추가

먼저 사용자 데이터 모델을 나타내는 클래스를 하나 선언한다. 그리고 SQLAlchemy의 기능을 사용하기 위해 `db.Model` 을 상속 받는다. 기본적으로 데이터베이스 테이블 이름은 자동으로 정의되지만 `__table_name__` 을 이용해 명시적으로 정할 수 있다.

---

클래스에 모델이 갖고 있어야 하는 필드와 관련된 제약사항들을 적어줘야 한다.

| 필드            | 제약사항    |
| --------------- | ----------- |
| `id`            | integer     |
| `username`      | string(100) |
| `email`         | string(100) |
| `password`      | string(100) |
| `profile_image` | string(100) |

- `id` 필드는 대부분의 모델에서 기본 키로 사용한다.
- `username`, `email`, `password`, `profile_image` 필드는 문자열로 정의를 하고, 최대 길이를 명시하여 공간을 절약할 수 있도록 한다. 
- `username`, `email` 필드는 서로 중복되지 않아야 하고, 비어있지 않아야 한다. 
- `password` 필드의 경우 중복되는 것은 괜찮지만 비어있으면 안된다. 그리고 보안을 위해 평문으로 저장하는 것이 아니라 암호화 해서 저장해야 한다. 
- `profile_image` 필드는 이미지 데이터를 DB에 직접 저장하는 것이 아니라 파일 시스템에 저장한 다음 그 파일 이름만 저장할 것이다. 그리고 프로필 이미지는 모든 사람이 처음부터 넣는 것이 아니기 때문에 기본 이미지 파일을 가리킬 필요가 있다. 기본 이미지 파일은 'default.png'로 설정할 것이다.

---

테이블 컬럼을 만들기 위해서는 `db.Column()` 을 이용한다. 컬럼의 이름은 기본적으로 변수 이름을 사용한다. `db.Column()` 은 데이터 타입에 대한 정보와 제약 조건들을 넣어줄 수 있다. 또 `__repr__` 메소드를 이용할 수 있다.

```python
# app.py
# ...

class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')

    def __repr__(self):
        return f"User: '{self.id}', '{self.username}', '{self.email}'"


# ...
```

비밀번호는 암호화된 해시로 저장해야 되기 때문에 추가적인 함수가 필요하다. werkzeug.security의 generate_password_hash, check_password_hash를 `app.py`에서 불러오자.

---

generate_password_hash,  check_password_hash 사용 예시

```shell
$ python3
>>> from werkzeug.security import generate_password_hash, check_password_hash
>>> hash = generate_password_hash('true_password@')
>>> print(hash)
pbkdf2:sha256:150000$yOIlKjbh$fbfc766817d7a65012b019c4fbbee14fa6062cc604d4f41ca7a41e1650b2fa38
>>> check_password_hash(hash, 'true_password@')
True
>>> check_password_hash(hash, 'wrong_password^')
False
```

---

암호화하는 과정은 객체가 생성할 때 해주는 것이 좋다.

```python
# app.py
# ...

from werkzeug.security import generate_password_hash, check_password_hash

# ...

class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f"User: '{self.id}', '{self.username}', '{self.email}'"

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
```

## 게시물 모델 추가

게시물은 제목과 내용으로 이루어 질 것이고, 추가적으로 언제 게시되었는지, 누가 게시했는지에 대한 정보가 필요하다. 이 중 게시자에 대한 정보는 사용자 데이터 모델에서 참조할 수 있다. 데이터베이스에서 하나의 유저가 여러 게시물을 갖을 수 있는 관계가 형성된다.

``` python
# app.py
# ...

class User(db.Model):
    # ...
    profile_image = db.Column(db.String(100), default='default.png')

    # 관계 설정
    posts = db.relationship('Post', backref='author', lazy=True)
	# db.relationship(class name, backref=Post가 backref를 할 때 필드 이름, lazy=??)

    def __init__(self, username, email, password, **kwargs):

# ...
class Post(db.Model):
    __table_name__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post: '{self.id}', '{self.title}'"

```

위 코드를 보면 기본적으로 게시물에 대한 데이터 모델 객체를 선언한다.

- `title`: 게시물 제목
- `content`: 게시물 내용
- `date_posted`: 게시일
    - 게시일의 경우에는 기본값을 `datetime.utcnow()` 를 사용함으로써 명시적으로 게시일을 나타내지 않은 경우 현재 시간을 게시일로 한다.
- `user_id`: `user` 테이블의 `id`를 외래키로 하는 필드
    - `db.ForeignKey` 는 **테이블 이름**을 인자로 받는다.
        - SQLAlchemy에서 테이블 이름은 기본적으로 소문자를 사용하고 여러 단어의 조합인 경우에는 스네이크 케이스를 사용한다.  

`User` 클래스를 보면 `posts` 컬럼이 추가되어 있다. `posts` 컬럼은 `db.relationship` 을 사용하는데 이는 실제 데이터베이스에 나타나는 필드는 아니다. 이 가상 필드는 데이터베이스를 좀 더 높은 추상화 수준에서 바라볼 수 있게 도와주는 역할을 한다. 예를 들어 사용자를 'user' 변수에 저장했다고 한다면, 이 사용자가 작성했던 모든 게시물에 대한 정보는 'user.posts'를 이용해 접근할 수 있다. `db.relationship` 의 첫 번째 인자는 `db.ForeignKey` 와는 다르게 **클래스 이름**을 받는다.

`backref` 는 `Posts` 클래스에 삽입되는 가상 필드 이름이다. 즉, 게시물을 'post'라는 변수에 저장하면, 이 게시물을 작성한 게시자를 'post.author'을 이용해 접근할 수 있다.

## 데이터베이스 초기화 및 데이터 추가

데이터베이스를 초기화하고 데이터를 추가하자.

```shell
$ flask_blog> python3
>>> from app import app, db, User, Post
>>> db.create_all()
```

이렇게 코드를 작성하면 flask_blog 디렉토리 안에 site.db라는 파일이 생긴다. 데이터베이스 초기화를 완료했으니 데이터를 추가하자.

``` shell
>>> user = User(username='user', email='user@blog.com', password='password')
>>> db.session.add(user)
>>> db.session.commit()
```

'user' 변수에 'User' 데이터 모델에 대한 인스턴스를 만들어 저장한 다음 이를 데이터베이스에 저장하기 위해 'db.session'을 이용한다. 데이터베이스를 수정하는 작업이 끝나면 'db.session.commit()'을 이용해 변경 내용을 저장할 수도 있고, 'db.session.rollback()'을 이용해 변경 사항을 취소할 수도 있다. 여기서 'db.session.add()'를 통해 데이터베이스에 객체를 추가했더라도 실제 데이터가 저장되는 시점은 'db.session.commit()'을 수행한 다음이다.

이제 게시물을 2개 추가해보도록 하자.

```shell
>>> post1 = Post(title='첫 번째 게시물', content='첫 번째 게시물 내용', author=user)
>>> post2 = Post(title='두 번째 게시물', content='두 번째 게시물 내용', author=user)
>>> db.session.add(post1)
>>> db.session.add(post2)
>>> db.session.commit()
```

게시물을 추가할 때 'user_id'를 넣어주지 않았다. 우리가 'Post' 데이터 모델을 만들 때, 게시자에 대한 정보를 넣어주기 위해 외래 키로 'user_id' 필드를 삽입했지만 'User' 데이터 모델에 관계에서 'backref'를 이용해 'author'에 대한 정보도 넣어줬다. 따라서 'Post' 모델에서 만들어진 가상의 'author' 필드를 사용해 'user_id' 필드에 직접 데이터를 넣어주지 않아도 게시자에 대한 정보를 쉽게 추적할 수 있다.

데이터베이스에 저장한 데이터를 가져오기 위해서는 각 모델에 'query'를 이용한다.

``` shell
>>> User.query.all()
[<User('user', 'user@blog.com')>]
>>> Post.query.all()
[<Post('1', '첫 번째 포스트')>, <Post('2', '두 번째 포스트')>]
```

## 데이터 보여주기

`db.query` 명령을 이용하여 데이터베이스에 저장되어 있는 모든 게시물 데이터를 불러와 `render_template` 함수에 전달할 수 있다.

``` python
# app.py
# ...

@app.route('/')
@app.route('/index/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run()

```

templates/index.html 파일을 만들고 이 파일 안에 render_template으로부터 받은 posts 데이터를 보여주는 코드를 작성하자.

``` html
{% for post in posts %}
<h1> {{ post.title }}</h1>
<p> {{ post.content }}</p>
<p> {{ post.author.username }}</p>
<img src="{{ url_for('static', filename='profile_imgs/' + post.author.profile_image) }}" alt="No image">
<p> {{ post.date_posted.strftime('%Y-%m-%d') }}</p>
{% endfor %}
```

## 



