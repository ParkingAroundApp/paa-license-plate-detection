from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'the static url is hello'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>', methods=['GET','POST'])
def findUserByName(username):
    return "Hi, we will find username: {0} for master".format(username)

if __name__ == '__main__':
    app.run()