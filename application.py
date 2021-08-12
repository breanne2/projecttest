from flask import Flask
from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask import Flask,request

mysql = MySQL()
application = Flask(__name__)


@application.route("/index")
def index():
    #application.config['RDS_HOSTNAME'] = 'database-1.cn1wgl48ybn6.eu-west-2.rds.amazonaws.com'
    #application.config['RDS_PORT'] = '3306'
    #application.config['RDS_DB_NAME'] = 'EUcustdb'
    #application.config['RDS_USERNAME'] = 'admin'
    #application.config['RDS_PASSWORD'] = 'Hollywarner10'

    application.config['MYSQL_DATABASE_USER'] = 'admin'
    application.config['MYSQL_DATABASE_PASSWORD'] = 'Hollywarner10'
    application.config['MYSQL_DATABASE_DB'] = 'EUcustdb'
    application.config['MYSQL_DATABASE_HOST'] = 'database-1.cn1wgl48ybn6.eu-west-2.rds.amazonaws.com'
    application.config['MYSQL_DATABASE_ROOT'] = '3306'

    mysql.init_app(application)

    cursor = mysql.connect().cursor()
    #cursor.execute('SELECT * FROM eu_cust_data')
    cursor.execute('SELECT * FROM EU_cust_data')
    data = cursor.fetchall()
    return render_template('index.html', output_data=data)

@application.route("/Authenticate")
def Authenticate():

    application.config['MYSQL_DATABASE_USER'] = 'root'
    application.config['MYSQL_DATABASE_PASSWORD'] = 'Hollywarner10'
    application.config['MYSQL_DATABASE_DB'] = 'inventorydb'
    application.config['MYSQL_DATABASE_HOST'] = 'localhost'

    #application.config['RDS_HOSTNAME'] = 'globalauroradb-cluster-1.cluster-ro-cn1wgl48ybn6.eu-west-2.rds.amazonaws.com'
    #application.config['RDS_PORT'] = '3306'
    #application.config['RDS_DB_NAME'] = 'inventorydb'
    #application.config['RDS_USERNAME'] = 'admin'
    #application.config['RDS_PASSWORD'] = 'Hollywarner10'

    mysql.init_app(application)

    cursor = mysql.connect().cursor()
    #Productname = request.args.get('productname')
    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * FROM items')
    data = cursor.fetchall()
    if data is None:
        return "Username or Password is wrong"
    else:
        return render_template('inventory.html', output_data=data)

@application.route('/')
def hello_world():
    #return 'London page!'
    return render_template('button.html')

if __name__ == '__main__':
    #application.run()
    application.run(host='localhost', port=5000)
