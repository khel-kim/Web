# Flask Getting Started

## Flask hello world app

플라스크를 이용하여 hello world를 출력하는 웹 애플리케이션을 만들어보자.

1. Create a file called hello.py

```python
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
```

Flask는 WSGI application을 실행하는 모듈이다. 웹 클라이언트의 Request가 들어오면 그 URL을 분석하고 `app.route(~)`에 정의된 URL이면 밑에 있는 함수를 실행하게 된다.

웹 브라우저에 http://127.0.0.1:5000/을 입력하게 되면, 클라이언트에서 GET 메소드로 요청을 보내게 된다.

```python
# hello.py log
127.0.0.1 - - [15/Jan/2020 15:48:17] "GET / HTTP/1.1" 200 -

Host 명 - - [시간] "요청 메소드 / 프로토콜 버전" 상태 코드 -
```





