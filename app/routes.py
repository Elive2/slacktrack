from app import app
from flask import request, jsonify
import requests #used in getUsers()
import os

SLACKWEBAPIURL = "https://slack.com/api/users.list"

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
	users = getUsers()

	return users


def getUsers():
	querystring = {"team_id":"T01DEQZBWQN"}
	token = os.getenv('AUTH_TOKEN')
	print("token" + token)
	payload = ""
	headers = {
    	'Authorization': "Bearer " + token,
    	'cache-control': "no-cache",
    }
	try:
		response = requests.request("GET", SLACKWEBAPIURL, data=payload, headers=headers, params=querystring)
		response.raise_for_status()
	except requests.exceptions.HTTPError as err:
		return err

	return response.json()
	
