from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'London page!'

if __name__ == '__main__':
    application.run()
