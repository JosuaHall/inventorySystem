from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_migrate import Migrate, migrate
from datetime import datetime, timezone
from app import app, db



# Settings for migrations
migrate = Migrate(app, db)

# Models
class Account(db.Model):
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	id = db.Column(db.Integer, primary_key=True)
	account_nr = db.Column(db.Integer, unique=True, nullable=False)   
	vendor_name = db.Column(db.String(100), nullable=False)
	children = relationship("GeneralVoucher")

class WorkInProcess(db.Model):
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	id = db.Column(db.Integer, primary_key=True)
	invoice_date = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc).astimezone())
	invoice_nr = db.Column(db.String(100), unique=True, nullable=False)
	customer = db.Column(db.String(100), unique=False, nullable=False)   
	job_name = db.Column(db.String(500), nullable=False)
	po_nr = db.Column(db.String(50), unique=True, nullable=False)
	vendor = db.Column(db.String(50), unique=False, nullable=False)
	cogs = db.Column(db.Float(50), unique=False, nullable=False)
	cogs_account = db.Column(db.String(500), nullable=False)
	invoiced = db.Column(db.String(5), unique=False, nullable=True)
	month_invoiced = db.Column(db.String(50), unique=False, nullable=True)
	exception = db.Column(db.String(50), unique=False, nullable=True)
	product_at_co = db.Column(db.String(5), unique=False, nullable=True)
	# repr method represents how one object of this data table
	# will look like
	#def __repr__(self):
	#	return f"Name : {self.first_name}, Age: {self.age}"

class GeneralVoucher(db.Model):
	vendor_id = db.Column(db.Integer, ForeignKey('account.id'), primary_key=True, autoincrement=False)
	voucher_year = db.Column(db.String(100), primary_key=True, nullable=False, autoincrement=False)
	voucher_month = db.Column(db.String(100), primary_key=True, nullable=False, autoincrement=False) 
	cogs = db.Column(db.Float(50), unique=False)