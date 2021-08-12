from flask import Flask
from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask import Flask,request

mysql = MySQL()
application = Flask(__name__)

@application.route("/index")
def index():
    application.config['RDS_HOSTNAME'] = 'database-1.cn1wgl48ybn6.eu-west-2.rds.amazonaws.com'
    application.config['RDS_PORT'] = '3306'
    application.config['RDS_DB_NAME'] = 'EUcustdb'
    application.config['RDS_USERNAME'] = 'admin'
    application.config['RDS_PASSWORD'] = 'Hollywarner10'

    mysql.init_app(application)

    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * FROM EU_cust_data')
    data = cursor.fetchall()
    return render_template('index.html', output_data=data)

@application.route('/')
def hello_world():
    return 'London page!'

if __name__ == '__main__':
    application.run()
