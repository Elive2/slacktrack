'''
File: routes.py

Description: this file defines all the public facing routes exposed by the app
It is a simple Restful API with one route for clients and one route for slack
to post events to.

Author: Eli Yale

TODO: Secure routes somehow, ensure they are only hit by valid slack events

[ ] - switch to aiohttp - should be trivial https://gist.github.com/rcarmo/3f0772f2cbe0612b699dcbb839edabeb
	or try flask multithreaded
	or try flask with gevent https://iximiuz.com/en/posts/flask-gevent-tutorial/
		-if we do this should be able to just set up long polling
		 and test with a few connections
'''

from app import app
from flask import request, jsonify, Response, send_from_directory
from . import dbmethods
from . import helpers
import json
import asyncio


'''
Function: hello

Description: index route returns the home view
'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
	if path != "" and os.path.exists(app.static_folder + '/' + path):
		return send_from_directory(app.static_folder, path)
	else:
		print(app.static_folder)
		return send_from_directory(app.static_folder, 'index.html')

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


'''
Function: allUsers()

Description:
return all users found in the database. This includes deactivated ones.
Slack maintains deactivated users just with the 'deleted' field set to true

'''
@app.route('/allUsers', methods=['GET'])
def allUsers():
	users = dbmethods.getUsers()
	return {'users': users}

'''
Function: activeUsers

Description:
returns only active users by filtering with the 'deleted' field

'''
@app.route('/activeUsers', methods=['GET'])
def activeUsers():
	users = dbmethods.getUsers()
	activeUsers = []
	for user in users:
		if not user['deleted']:
			activeUsers.append(user)

	return {'users': activeUsers}







	
