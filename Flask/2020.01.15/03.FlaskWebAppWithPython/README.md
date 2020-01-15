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

