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

Deployment Checklist:
	Set environment variable

	AUTH_TOKEN=
	MONGODB_URI=
	REACT_APP_API_URL=
	HOST_IP=
	PORT_APP=
	
'''
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from app import app
import os

if __name__ == '__main__':
	app.run(host='0.0.0.0', use_reloader=True, port=5000, threaded=True)
	'''
        if os.getenv('HOST_IP'):
		ip = os.getenv('HOST_IP')
	else:
		ip = '127.0.0.1'
	if os.getenv('PORT_APP'):
		port = int(os.getenv('PORT_APP'))
	else:
		port = 5000
	http_server = WSGIServer((ip, port), app)
	http_server.serve_forever()
        '''
