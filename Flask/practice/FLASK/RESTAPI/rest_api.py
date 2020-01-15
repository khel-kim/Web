from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
# Flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)

# json 형식 데이터 정의
TODOS = {
    'todo1': {'task': 'Make Money'},
    'todo2': {'task': 'Play PS4'},
    'todo3': {'task': 'Study!'},
}

parser = reqparse.RequestParser()



if __name__ == "__main__":
    app.run()
