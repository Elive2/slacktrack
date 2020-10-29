from flask import Flask
import os

app = Flask(__name__)

app.config['AUTH_TOKEN'] = os.getenv('AUTH_TOKEN')

from app import routes