'''
File: /slacktrack.py

Description:
Main entrypoint for the app and where gunicorn will pick up the app
'''
from app import app

if __name__ == '__main__':
	app.run(use_reloader=True, threaded=True)
