from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ac2a5e142e41130412792a4a54dd0732'
app.config['TEMPLATES-AUTO-RELOAD'] = True


app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'news_portal'

mysql = MySQL()
mysql.init_app(app)