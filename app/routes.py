from flask import redirect, request, render_template, flash
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import extract, func
from app.modules import GeneralVoucher, WorkInProcess, Account
db = SQLAlchemy(app)
from ordered_set import OrderedSet

# function to render index paccount_names
@app.route('/')
def index():
	#accounts = account.query.all()
	return render_template('base.html')

@app.route('/vendor')
def add_data():
	return render_template('vendor.html')
    
@app.route('/add_vendor')
def add_account():
	return render_template('vendorForm.html')

@app.route('/list_vendors')
def list_account():
	vendors = Account.query.order_by(Account.account_nr.asc()).all()
	return render_template('listVendor.html', vendors=vendors)

# function to add accounts
@app.route('/add', methods=["POST"])
def account():
	# In this function we will input data from the
	# form paccount_names and store it in our database. Remember
	# that inside the get the name should exactly be the same
	# as that in the html input fields
	category = request.form.get("vendors")
	account_nr = request.form.get("account_nr")
	vendor_name = request.form.get("vendor_name")

	# create an object of the account class of models and
	# store data as a row in our datatable
	if account_nr is not None and category != '' and vendor_name is not None:
		v = Account(category=category, account_nr=account_nr, vendor_name=vendor_name)
		db.session.add(v)
		db.session.commit()
		return redirect('/vendor')
	else:
		return redirect('/')


@app.route('/work_in_process')
def work_in_process():
	return render_template('workInProcess.html')
	
@app.route('/add_work_in_process')
def add_work_in_process():
	vendors = Account.query.all()
	return render_template('addWorkInProcess.html', vendors=vendors)

@app.route('/add_wip', methods=["POST"])
def wip():
	# In this function we will input data from the
	# form paccount_names and store it in our database. Remember
	# that inside the get the name should exactly be the same
	# as that in the html input fields
	invoice_nr = request.form.get("invoice_nr")
	customer = request.form.get("customer")
	job_name = request.form.get("job_name")
	po_nr = request.form.get("po_nr")
	vendor = request.form.get("vendor")
	cogs = request.form.get("cogs")
	vendors = request.form.get("vendors")
	invoiced = request.form.get("invoiced")
	exception = request.form.get("exception")
	month_invoiced = request.form.get("month_invoiced")
	product_at_co = request.form.get("product_at_co")
	value = ""
	value2 = ""
	value3 = ""
	if invoiced == "1":
		value += "Yes"
	else:
		value = "No"
	
	if product_at_co == "1":
		value2 += "Yes"
	else:
		value2 += "No"

	if exception == "1":
		value3 += "Yes"
	else:
		value3 += "No"

	# create an object of the account class of models and
	# store data as a row in our datatable
	if invoice_nr is not None \
		and customer != '' \
			and job_name != '' \
				and po_nr != '' \
					and vendor != '' \
						and cogs is not None \
							and vendors != '' :
		wip = WorkInProcess(invoice_nr=invoice_nr, customer=customer, job_name=job_name, po_nr=po_nr, vendor=vendor,cogs=cogs,cogs_account=vendors,invoiced=value, exception=value3, month_invoiced=month_invoiced,product_at_co=value2)
		db.session.add(wip)
		db.session.commit()
		return redirect('/work_in_process')
	else:
		return redirect('/')

@app.route('/update_wip/<int:id>', methods=["PUT", "POST", "GET"])
def update2(id):
	invoice_nr = request.form.get("invoice_nr")
	customer = request.form.get("customer")
	job_name = request.form.get("job_name")
	po_nr = request.form.get("po_nr")
	vendor = request.form.get("vendor")
	cogs = request.form.get("cogs")
	vendors = request.form.get("vendors")
	invoiced = request.form.get("invoiced")
	exception = request.form.get("exception")
	month_invoiced = request.form.get("month_invoiced")
	product_at_co = request.form.get("product_at_co")
	value = ""
	value2 = ""
	value3 = ""
	if invoiced == "1":
		value += "Yes"
	else:
		value = "No"
	
	if product_at_co == "1":
		value2 += "Yes"
	else:
		value2 += "No"

	if exception == "1":
		value3 += "Yes"
	else:
		value3 += "No"

	# create an object of the account class of models and
	# store data as a row in our datatable
	if invoice_nr is not None \
		and customer != '' \
			and job_name != '' \
				and po_nr != '' \
					and vendor != '' \
						and cogs is not None \
							and vendors != '' :
		wip = db.session.query(WorkInProcess).get(id)
		wip.invoice_nr = invoice_nr
		wip.customer = customer
		wip.job_name = job_name
		wip.po_nr = po_nr
		wip.vendor = vendor
		wip.cogs = cogs
		wip.cogs_account = vendors
		wip.invoiced = value
		wip.exception = value3
		wip.month_invoiced = month_invoiced
		wip.product_at_co = value2
		db.session.commit()
		return redirect('/work_in_process_list')
	else:
		return redirect('/')
	
	
@app.route('/work_in_process_list')
def list_work_in_process():
	wip = WorkInProcess.query.all()
	return render_template('workInProcessList.html', wip = wip)

@app.route('/general_voucher')
def general_voucher():
	return render_template('generalVoucher.html')

@app.route('/create_general_voucher')
def create_general_voucher():
	return render_template('createGeneralVoucher.html')
	
@app.route('/add_general_voucher', methods=['POST'])
def add_general_voucher():
	vendors = Account.query.all()
	l=[]
	l_id=[]
	for vendor in vendors:
		l.append(vendor.vendor_name)
		l_id.append(vendor.id)
	month = request.form.get("month")
	year = request.form.get("year") # missing year check -> get year from date out of wip
	wip = WorkInProcess.query.filter(extract('year',WorkInProcess.invoice_date) == year, WorkInProcess.month_invoiced==month, WorkInProcess.invoiced=="Yes").all()
	cogs_sums = dict.fromkeys(l, 0)
	for vendor in cogs_sums:
		for data in wip:
			if data.cogs_account.lower() == vendor.lower():
				cogs_sums[vendor] += data.cogs
	i = 1
	for c in cogs_sums:
		vendor_id = l_id[i-1]
		voucher_year = year
		voucher_month = month
		cogs = cogs_sums[c]
		i += 1
		general_voucher = GeneralVoucher(vendor_id=vendor_id, voucher_year=voucher_year,voucher_month=voucher_month, cogs=cogs)
		db.session.add(general_voucher)
	try:
		db.session.commit()
		flash("General Voucher Added")
	except:
		flash("A general voucher already exists for this year/month")

	return render_template('createGeneralVoucher.html')

@app.route('/list_general_voucher')
def list_general_voucher():
	#general_voucher = GeneralVoucher.query.all()
	#years= OrderedSet()
	
	#for gv in general_voucher:
		#years.add(gv.voucher_year)
	return render_template('listGeneralVoucher.html')

@app.route('/get_general_voucher', methods=["POST"])
def get_general_voucher():
	month = request.form.get("month")
	year = request.form.get("year")
	cogs_sum = 0
	general_voucher = GeneralVoucher.query.filter(GeneralVoucher.voucher_year == year, GeneralVoucher.voucher_month == month).join(Account, GeneralVoucher.vendor_id == Account.id).add_columns(GeneralVoucher.cogs, Account.account_nr, Account.vendor_name).all()
	for data in general_voucher:
		cogs_sum += data.cogs
	if len(general_voucher) == 0:
		flash("The selected Voucher does not exist")		
	return render_template('listGeneralVoucher.html', general_voucher=general_voucher, month=month, year=year, cogs_sum=cogs_sum)

@app.route('/inventory')
def inventory():
	return render_template('inventory.html')

@app.route('/stock_inventory_purchases')
def stock_inventory_purchases():
	return render_template('stockInventoryPurchases.html')

@app.route('/add_stock_inventory_purchase')
def add_stock_inventory_purchase():
	return render_template('addStockInventoryPurchase.html')

@app.route('/update_work_in_process/<int:id>')
def update(id):
	vendors = Account.query.all()
	data = WorkInProcess.query.get(id)
	return render_template('updateWorkInProcess.html', data=data, vendors=vendors)