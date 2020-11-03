from flask import Flask
import os
from . import dbmethods
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MONGOHOST = "mongodb://localhost:27017"

try:
	dbmethods.connect(MONGOHOST)
except:
	print("error connecting to Mongo")

from app import routes