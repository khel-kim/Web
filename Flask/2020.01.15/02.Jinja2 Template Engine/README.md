# Jinja2 Template engine

Jinja2는 data를 웹 페이지에게 rendering할 때 사용된다.

Jinja2 template engine을 이용하므로써 html과 css를 파이썬 코드로부터 분리할 수 있다.

```
# 폴더 구조
/app
	app.py
	/templates
		user.html
```

1. create the file user.html in /app/templates:

    ```html
    <h1>{{ title }}</h1>
    <ul>
    {% for user in users %}
      <li>{{ user }}</li>
    {% endfor %}
    </ul>
    ```

2. create the code app.py in /app/app.py:

    ```python
    from flask import Flask, render_template
    app = Flask(__name__)
    
    
    @app.route('/')
    def index():
        return "Flask App!"
    
    
    @app.route('/user/')
    def hello():
        title = 'my friends'
        users = ['Frank', "Steve", "Alice", "Bruce"]
        print(locals())
        return render_template('user.html', **locals())
    
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
    
    ```

    

- `render_template` 메소드로 `html`을 불러올 수 있다.

    - `html` 파일은 `templates` 폴더 안에 존재해야 한다.

- `locals()` 함수는 local에 정의된 변수들을 dictionary 형태로 반환한다.

    - 우리 코드에서는 `locals()`는 다음을 반환한다.

        `{'users': ['Frank', 'Steve', 'Alice', 'Bruce'], 'title': 'my friends'}`

- `render_template`의 두번째 인자부터 `html`에서 받을 변수들을 정의할 수 있다.

- `app.run(host='~', port=number)`의 형태로 호스트명(ip)와 포트를 정의해줄 수 있다.