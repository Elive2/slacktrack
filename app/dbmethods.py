import pymongo

MONGOHOST = "mongodb://localhost:27017"

def persistToDB(data):
	host = pymongo.MongoClient(MONGOHOST)
	db = host['slacktrackdb']
	collection = db['slackUsers']
	collection.remove()
	x = collection.insert_many(data)
	print("persited")
	return