from flask import Flask
import os
from . import dbmethods
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='../client/build')
# CORS(app)

MONGOHOST = os.getenv("MONGODB_URI", "mongodb://localhost:27017") 

try:
	dbmethods.connect(MONGOHOST)
except:
	print("error connecting to Mongo")

from app import routes