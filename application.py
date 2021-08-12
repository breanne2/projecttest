from flask import Flask
from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask import Flask,request

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'London page!'

if __name__ == '__main__':
    application.run()
