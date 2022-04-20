from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zenmysbrtfkamu:60140b6b14aa551e016e5362211bc06137667e9bc0c776f37af6cefb2147bf76@ec2-34-194-158-176.compute-1.amazonaws.com:5432/d97n65tflkm06e'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
from app import routes