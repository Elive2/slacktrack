from app import app
from flask import request, jsonify
from . import dbmethods
from . import helpers
import json

@app.route('/')
def hello():
	return 'Hello World'

#public facing route forwarded to from http://39d9ad8d569e.ngrok.io/slack
@app.route('/slack', methods=['POST'])
def slack():
	print(request.json)
	if 'challenge' in request.json:
		return challenge, 200
	
	return "ok", 200

#perform a hard sync of users and completly update database
#with current users in the slack workspace
@app.route('/hardSyncUsers', methods=['GET'])
def hardSyncUsers():
	#this is a blocking request for now, could be asynced or threaded later on
	#see celery, asyncio or the likes
	try:
		users = helpers.getUsers()
	except RuntimeError as e:
		return "Could not fetch users from Slack Web API. ERROR:" + e


	cleanedUsers = helpers.clean(users)

	try:
		dbmethods.persistToDB(cleanedUsers)
	except:
		return "Error persisting to database, check mongo"

	print("returning user[1]", cleanedUsers[1])
	return json.dumps(cleanedUsers[1])


	
