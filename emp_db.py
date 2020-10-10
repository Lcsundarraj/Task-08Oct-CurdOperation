from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://sundar:sundar@cluster0.dol3j.mongodb.net/EmployeeDB?retryWrites=true&w=majority')
	db = con.EmployeeDB
	col = db.emp_records



def get_emplyoee_details():
	global col
	connect_db()
	empdata_from_db = col.find({})
	return empdata_from_db

def get_one_emplyoee_details(emp_id):
	global col
	connect_db()
	empdata_from_db = col.find({"_id": ObjectId(emp_id)})
	return empdata_from_db


def save_employee_data(emp_info):
	global col
	connect_db()
	col.insert(emp_info)
	return "saved Successfully"


def delete_record(emp_id):
    global col
    connect_db()
    myquery = {"_id": ObjectId(emp_id)}
    col.delete_one(myquery)
    return


def update_one_record(empid, empRecords):
    global col
    connect_db()    
    col.update_one({"_id": ObjectId(empid)}, {'$set' :{'name':empRecords["name"], 'designation':empRecords["designation"], 'contact':empRecords["contact"]} })
    return

def update_field(empid):
	global col
	connect_db()
	col.update({"_id": ObjectId(empid)}, {'$unset' :{'designation':""}})
	return
