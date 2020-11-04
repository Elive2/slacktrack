'''
File: app/helpers.py

Description:
Some various helpers functions that are better seperated into a different module

'''

import requests
import os

SLACKWEBAPIURL = "https://slack.com/api/users.list"

'''
Custom logging function left for future debugging
'''
def log(msg):
    print(msg)

'''
Function: getUsers()

Description: 
this function is invoked when a client hits the /hardSyncUsers route
It is used to query the Slack Web API and get all users currently listed in the
slack directory. This function is useful for debugging when there is a database
sync issue

Returns:
    members (json) json response object of all the users found in slack
'''
def getUsers():
    querystring = {"team_id":"T01DEQZBWQN"}
    token = os.getenv('AUTH_TOKEN')
    if token is None:
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

'''
Function: Clean()

Description;
Helper function left in case you want to clean some data from the users

'''
def clean(userData):
    # cleanedData = {
    #     "usrID": member['id'],
    #     "color": member['color'],
    #     "is_admin": member['is_admin'],
    #     "is_bot": member['is_bot'],
    #     "display_name": member['profile']['display_name'],
    #     "image": member['profile']['image_192'],
    #     "real_name": member['profile']['real_name'],
    #     "updated": member['updated'],
    #     "deleted": member['deleted'],
    #     }
    cleanedData = userData

    return cleanedData