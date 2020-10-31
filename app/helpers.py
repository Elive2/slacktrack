import requests
import os

SLACKWEBAPIURL = "https://slack.com/api/users.list"

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
		raise RuntimeError("HTTPError: " + err)
		return 

	return response.json()

def clean(userData):
	cleanedData = []
	for member in userData['members']:
		cleanedData.append( {
			"usrID": member['id'],
			"color": member['color'],
			"is_admin": member['is_admin'],
			"is_bot": member['is_bot'],
			"display_name": member['profile']['display_name'],
			"image": member['profile']['image_192'],
			"real_name": member['profile']['real_name'],
			"updated": member['updated'],
			"deleted": member['deleted'],
			})

	return cleanedData