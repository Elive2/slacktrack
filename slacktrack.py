'''
File: /slacktrack.py

Description:
Main entrypoint for the app and where gunicorn will pick up the app
'''
from app import app
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/slacktrack')
load_dotenv(os.path.join(project_folder, '.env'))

if __name__ == '__main__':
	app.run(use_reloader=True, threaded=True)
