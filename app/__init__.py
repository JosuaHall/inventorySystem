import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# adding configuration for using a sqlite database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ifa16A2019nD%21@localhost/inventorySystem'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
from app import routes