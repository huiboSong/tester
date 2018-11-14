__author__='songhuibo'
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input("输入用户名称:")
    return


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == "__main__":
    app.run()