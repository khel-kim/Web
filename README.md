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



## Flask tf serving

