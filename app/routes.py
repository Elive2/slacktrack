'''
TODO: Secure routes somehow, ensure they are only hit by valid slack events

[ ] - current behavior: When an account is deactivated the delete user method removes
them from the database, but then hardsync adds them back just a a deleted account. Reactivating
a user doesn't work without a hardsync because flask processes this as a user update event
not the team_join event yet.
'''

from app import app
from flask import request, jsonify, Response
from . import dbmethods
from . import helpers
import json
import asyncio


'''
Function: hello

Description: index route returns the home view
'''
@app.route('/')
def hello():
	return 'Hello World'

'''
Function: slack

Description:
	public facing route forwarded to from http://39d9ad8d569e.ngrok.io/slack
	Slack Events API hits this route when an event we are subscribed to fires
	this method examines the event type and responds accordingly

Returns:
	status - (flask.response object) 200

TODO:
eventually would want to async this with an event handler queue
slack reccomends returning 200 immediately and processing event after
the asyncio event queue would be very useful here
'''

@app.route('/slack', methods=['POST'])
def slack():
	data = request.json
	if 'challenge' in data:
		challenge = data['challenge']
		return challenge, 200

	#helpers.log(data)
	event = data['event']
	eventType = event['type']

	
	if eventType == 'user_change':
		helpers.log("updating user")
		user = event['user']
		if user['deleted']:
			try:
				dbmethods.removeUser(user)
			except:
				return "Error removing user in database, check mongo"
		try:
			dbmethods.updateUser(user)
		except:
			return "Error updating user in database, check mongo"

	elif 'channel' in eventType:
		pass
		#helpers.log("detected channel change")

	elif eventType == 'team_join':
		helpers.log("new member joined")
		try:
			dbmethods.addUser(user)
		except:
			return "error adding user to databse, check mongo"
	else:
		helpers.log("unknown event type")

	
	status = Response(status=200)
	return status

'''
Function: hardSyncUsers

Description:
perform a hard sync of users and completly update database
with current users in the slack workspace. This route invokes the
getUsers method which is a network call to the slack web API to get 
all current users in the workspace. This is an IO and should eventually be
asynced to prevent the server from blocking.

TODO:
async the getUsers call with asyncio or celery

'''
@app.route('/hardSyncUsers', methods=['GET'])
def hardSyncUsers():
	try:
		users = helpers.getUsers()
	except RuntimeError as e:
		return "Could not fetch users from Slack Web API. ERROR:" + e

	cleanedUsers = [helpers.clean(user) for user in users]
	helpers.log("cleaned users")
	helpers.log(cleanedUsers)

	try:
		dbmethods.persistToDB(cleanedUsers)
	except:
		return "Error persisting to database, check mongo"

	return "success"

@app.route('/users', methods=['GET'])
def users():
	users = dbmethods.getUsers()
	print(users)
	return {'users': users}







	
