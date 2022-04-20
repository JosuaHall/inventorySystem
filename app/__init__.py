from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fiemuwjuewrjxc:a791518afadf00cf05b160fe6b14b11d671fb551f3d3d8bd6e5c3527f7d4f6c5@ec2-52-203-118-49.compute-1.amazonaws.com:5432/d6dngl6juhaa2h'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
from app import routes