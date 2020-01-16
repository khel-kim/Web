# Login Authentication With Python

Flask의 session을 이용한 로그인 기능 구현

## Building A Flask Login Screen

1. Create this Python file as hello.py.

    ```python
    from flask import Flask, render_template
    from flask import request, session
    import os
    app = Flask(__name__)
    
    
    @app.route('/')
    def home():
        print('SESSION:', session)
        # session 객체는 dictionary 
        if not session.get('logged_in'):
            return render_template('login.html')
        else:
            return "Hello Boss!"
    
    
    @app.route('/login/', methods=['POST'])
    def do_admin_login():
        print("SESSION:", session)
        print("REQUEST:", request)
        # request는 url '/'의 'login.html'에서 보내온 form에 있는 자료를
        # dictionary 구조로 가지고 있음
        
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            # 'admin'은 ID로 사용되는 값
            # 'password'는 비밀번호로 사용되는 값
            session['logged_in'] = True
            return home()
        else:
            return home()
    
    
    if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True, host='0.0.0.0', port=4000)
    
    ```

2. Create the directory /templates/. Create the file /templates/login.html with this code.

    ``` html
    {% block body %}
    {% if session['logged_in'] %}
        You're logged in already!
    {% else %}
        <form action="/login/" method="POST">
            <input type="username" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Log in">
        </form>
    {% endif %}
    {% endblock %}
    
    ```

3. `$ python3 hello.py`: 를 터미널에서 입력하면 로그인 페이지가 보인다(아이디와 비밀번호는 admin, password). 로그인하면 "hello boss!"가 웹 브라우저에 나타날 것이다.

- `app.secret_key` : 공격자로부터의 방어를 위해 비밀키를 요구하는 '어떤 것이든지' 비밀키 값이 세팅되도록 요구된다. Flask에서 Session 객체도 방어를 위해 비밀키를 요구하는 객체이다.

    