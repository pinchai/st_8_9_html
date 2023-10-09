from flask import Flask, session, render_template, request, redirect, url_for, flash
from datetime import timedelta

from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'flask_auth'

mysql = MySQL(app)

import routes


if __name__ == '__main__':
    app.run()
