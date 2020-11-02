import pymongo
from . import helpers

_host = None
_db = None

'''
Function: connect

Description:
connect to mongodb and store the connection in global variables
This method is invoked once from the _inint_.py upon app creation

Parameters:
	host - (string) the address of the mongodb instance to connect to

Returns:
	_db (MongoDB instance)
'''
def connect(host):
	global _db
	global _host
	helpers.log("connecting to DB")
	_host = pymongo.MongoClient(host)
	_db = _host['slacktrackdb']
	return _db

'''
Function: persistToDB

Description:
Take all the user data and re sync it with the database. This function
first erases the collection and re-adds all users as new documents

Parameters:
	data - (list) of users to add to the db
'''
def persistToDB(data):
	global _db
	collection = _db['slackUsers']
	collection.remove()
	x = collection.insert_many(data)
	helpers.log(x)
	helpers.log("persisted successfully")
	return

'''
Function: updateUser

Description:
perform an update to the given user by replacing the document with the save function

Parameters:
	data - (dict) of a single users info
'''
def updateUser(data):
	global _db
	helpers.log(data)
	collection = _db['slackUsers']
	query = {'id': data['id']}
	x = collection.replace_one(query, data)
	helpers.log(x)
	helpers.log("updated successfully")
	return

def addUser(data):
	global _db
	collection = _db['slackUsers']
	x = collection.insert_one(data)
	helpers.log(x)
	helpers.log("persisted successfully")
	return

def removeUser(data):
	global _db
	collection = _db['slackUsers']
	query = {'id': data['id']}
	x = collection.delete_one(query)
	helpers.log(x)
	helpers.log("deleted successfully")