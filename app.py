from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import emp_db

app = Flask(__name__)


app.secret_key="sdsdsdsf343f3eer3"


@app.route("/")
def index():
	#get all data from db
	emp_info = emp_db.get_emplyoee_details()
	empdetails_list = []
	for e in emp_info:
		empdetails_list.append(e)
	return render_template('form.html', emplist = empdetails_list )



#update records in DB
@app.route("/", methods=['POST'])
def update_emp_records():	
	#Empty List
	empRecords = {}
	#request data from UI
	name = request.form['uname']
	designation = request.form['desg']
	contact = request.form['phone']
	address = request.form['addrs']
	mailId =  request.form['email']
	#set data to the Empty list
	empRecords["name"]=name
	empRecords["designation"]=designation
	empRecords["contact"]=contact
	empRecords["address"]=address
	empRecords["mailId"]=mailId
	#print records in cmd
	print(empRecords)
	#send to db
	if (request.form['_id']==True):
		empid=request.form['_id']
		update_emp = emp_db.get_one_emplyoee_details(empid)
		emp_db.update_one_record(empid, update_emp)

	else:
		emp_db.save_employee_data(empRecords)
	return redirect(url_for('index'))


@app.route("/delete/<emp_id>", methods=['POST'])
def deleteRecord(emp_id):
    empid = emp_id
    emp_db.delete_record(empid)
    return redirect(url_for('index'))



@app.route("/edit/<emp_id>", methods=['POST'])
def edit_Record(emp_id):
    empid = emp_id
    one_emp_info = emp_db.get_one_emplyoee_details(empid)
    return render_template('edit_form.html', emplist = one_emp_info)



if __name__ == '__main__':
	app.run(debug=True)