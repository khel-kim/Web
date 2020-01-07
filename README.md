# FLASK

사이드바 토글: cmd + shift + L

Python Flask를 통해 text2remoji의 데모 버전을 만들자

## Flask 기초

참조 불로그: https://doorbw.tistory.com/31

### Flask 시작하기

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()

```

### 숫자를 입력받고 버튼을 눌렀을 때, 입력한 숫자의 구구단을 출력하는 웹 페이지 제작

```latex
templates/
	main.html
GuGuDan.py
```

```python
# GuGuDan.py
from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/<int:num>')  # 주소를 2개 걸 수 있음
def inputTest(num=None):
    return render_template('main.html', num=num)  # templates 폴더 안에서 search


@app.route('/calculate', methods=['POST'])  # method 정의법
def calculate(num=None):
    if request.method == "POST":
        temp = request.form["num"]  # 주소가 호출될 때 request가 자동으로 정의되는 듯, request.form은 main.html에서 input의 "num"이 들어오는 듯
    else:
        temp = None
    return redirect(url_for('inputTest', num=temp))  # inputTest라는 함수를 찾아냄


if __name__ == '__main__':
    app.run()

```

```html
<!-- /templates/main.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask #2</title>
</head>
<body>
    <form method="POST" action="/calculate">
        <h1> Flask #2 데이터 입력받기</h1>
        <h3> 사용자가 원하는 구구단을 출력하자!<br></h3>
        <h5> 출력하고자 하는 구구단을 입력하세요.</h5>
        <input type="text" name="num">
        <button type="submit">구구단 확인하기</button>
    </form>

    <div>
        <p>
            {% if num == None %}
            <h5>아직 아무 숫자도 입력이 안되었습니다.</h5>
            {% else %}
                {% for i in range(1,10) %}
                    <p>{{num}} x {{i}} = {{num*i}}<br></p>
                {% endfor %}
            {% endif %}
        </p>
    </div>
</body>
</html>
```

1. html에서 input을 어떻게 받는지 알기
    1. method 정의
    2. action 정의
2. html에서 if 문, for 문, 바로 계산 어떻게 하는지 알기
3. url 정의 => 함수 정의 => html 정의 => action 함수 정의 => html 정의

### Flask에서 MongoDB에 연결하여 데이터를 사용하기



## Flask를 이용하여 REST API 만들기

참고 사이트: https://rekt77.tistory.com/103

### REST API란?

REST API란 Representational State Transfer의 약자로 자원의 이름을 기반으로 하여 상태를 주고 받는 것이다. JSON이나 XML의 형태로 데이터를 주고 받는 것이 일반적이며 URI(Uniform Resource Identifier)를 통해 자원을 명시하고 HTTP 프로토콜에서 제공하는 메소드를 활용해 해당자원에 대한 CRUD를 동작하게 하는 API이다.

URI(Uniform Resource Identifier)란 요청하는 주소가 실제 존재하는 파일이라기보다는 기능을 하기위한 구분자로 보는 것이다.

### Flask를 이용한 기본적인 REST API 구현

REST API를 구축하기 위해서는 데이터를 json 형식으로 리턴해야한다. 그리고 요청이 들어왔을 때,  HTTP 메소드 별로 실행 루틴을 다르게 구현할 수 있다. 

### 실습

코드 사이트: https://niceman.tistory.com/101

2020.01.07

## Flask tf serving

