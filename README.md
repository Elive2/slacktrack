SlackTrack is a demonstration project that syncs users from a slack workspace
with a MongoDB and then exposes a flask API for a client to view the current members.
The app subscribes to the Slack Event API to receive changes to the members.

Currently Supported Changes include:
-New User Added
-User Deactivated
-User Profile change (Name Change, Profile Pic etc.)
		
To Develop Locally:

upgrade and install python packages (virtual environment recommended)

	pip install -r requirements.txt

upgrade and install node packages

	cd client && npm install

ensure ngrok is installed start ngrok in the background forwarding requests:

	./ngrok http 5000

mongo db should be running with

	brew services start mongodb-community

flask runs locally with

	flask run

or

	python3 slacktrack.py

if you want continous reloading for react dev, start the react development server with
	
	cd client && yarn start

Deployment Checklist:

The app is currently deployed on a digital ocean droplet and can be found at:

	http://167.71.127.136:5000/

1. Create a production optimized build with

	cd client && npm run build

2. ensure Set environment variables are set

	AUTH_TOKEN=
	MONGODB_URI=
	REACT_APP_API_URL=

3. ensure nginx is running

4. ensure mongodb is running

5. start gunicorn and the app with

	sudo supervisorctl start slacktrack
	
Architecture:


react client <-> flask <-> mongo
					\
					 Slack

url to manage slack app:
	https://api.slack.com/apps/A01DTN37L4U

url to manage workspace:
	https://slacktrackdemo.slack.com/home
