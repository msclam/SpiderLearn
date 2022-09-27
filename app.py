import datetime

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/user/<name>')
def welcome(name):
    return "你好 %s" % name


@app.route('/user/<int:id>')
def welcome2(id):
    return "你好 %d" % id


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/datetime')
def get_datetime():
    time = datetime.date.today()
    name = ["a", "b", "c"]
    task = {"任务": "abc", "时间": "今天"}
    return render_template('index.html', var=time, list=name, task=task)


@app.route('/test/register')
def register():
    return render_template('test/register.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('test/result.html', result=result)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
