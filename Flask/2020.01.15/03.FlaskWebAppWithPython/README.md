# Flask Web App with Python

## Creating URL routes

URL Routing을 통해 URL들을 외우기 쉽게 만들 수 있다. 우리는 다음과 같은 URL routes을 만들 것이다.

```python
/hello
/members/
/members/names/
```

1. create the code app.py

    ```python
    from flask import Flask
    app = Flask(__name__)
    
    
    @app.route('/')
    def index():
        return "Index!"
    
    
    @app.route('/hello/')
    def hello():
        return "Hello World!"
    
    
    @app.route('/members/')
    def members():
        return "Members"
    
    
    @app.route('/members/<string:name>/')
    def get_member(name):
        return f"The name is {name}"
    
    
    if __name__ == "__main__":
        app.run()
        
    ```

2. Test

    - http://127.0.0.1:5000/
    - http://127.0.0.1:5000/hello
    - http://127.0.0.1:5000/members
    - http://127.0.0.1:5000/members/Jordan/

- `@app.route('/members/<string:name>/')` 에서 `string`을 `int`나 다른 걸로 바꿔보기

## Style Flask Pages

우리는 코드와 UI를 templates라는 technique을 이용하여 분리할 것이다.  `/templates/`라는 디렉토리를 생성하고 다음과 같은 template을 만들자.

```html
<h1> Hello {{ name }} </h1>
```

Flask 애플리케이션의 URL과 포트를 바꿔보자.

```python
# app.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "Flask App!"


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
   
```

#### html 상속

``` html
# templates/layout.html

<!DOCTYPE HTML>
<html lang="kr">
  <head>
    <meta charset="utf-8">
    <title>Flask 블로그</title>
  </head>

  <body>
    <header>
      <nav>
        <a href="/">Flask 블로그</a>
        <a href="/">Home</a>
      </nav>
      <hr>
    </header>

    <main role="main">
        
    <!-- Main content block -->
    {% block content %}{% endblock %}
    
    </main>
  </body>
</html>
```

``` html
# templates/test.html

{% extends 'layout.html' %}

{% block content %}
    <h1> Hello, {{ name }}</h1>
{% endblock %}
```

