import requests
import os

SLACKWEBAPIURL = "https://slack.com/api/users.list"

def log(msg):
	print(msg)


def getUsers():
	querystring = {"team_id":"T01DEQZBWQN"}
	token = os.getenv('AUTH_TOKEN')
	if token is none:
		raise RuntimeError("No AUTH_TOKEN set")

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

	return response.json()['members']

def clean(userData):
	# cleanedData = {
	# 	"usrID": member['id'],
	# 	"color": member['color'],
	# 	"is_admin": member['is_admin'],
	# 	"is_bot": member['is_bot'],
	# 	"display_name": member['profile']['display_name'],
	# 	"image": member['profile']['image_192'],
	# 	"real_name": member['profile']['real_name'],
	# 	"updated": member['updated'],
	# 	"deleted": member['deleted'],
	# 	}
	cleanedData = userData

	return cleanedData