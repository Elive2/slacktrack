'''
url to manage slack app:
	https://api.slack.com/apps/A01DTN37L4U

url to manage workspace:
	https://slacktrackdemo.slack.com/home

Environment variables required to run this app

FLASK_APP=slacktrack.py
AUTH_TOKEN=

Architecture:

ngrok is running in the background forwarding requests:
http://39d9ad8d569e.ngrok.io -> http://localhost:5000
start ngrok for local development with

	./ngrok http 5000

flask runs locally with

	flask run

and gets configuration from .flaskenv

mongo db should be running with

	brew services start mongodb-community

start the react development server with
	
	yarn start
'''
from app import app