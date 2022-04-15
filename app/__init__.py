from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# adding configuration for using a sqlite database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ifa16A2019nD%21@localhost/inventorySystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://upfjvjyeygmihv:c0268e323fe1ab1b9c396e5ae2544ce6f86708c738c49ec3778f147019ce8402@ec2-34-194-158-176.compute-1.amazonaws.com:5432/d6njhra8vf1f9r'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
from app import routes