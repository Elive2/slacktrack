from flask import Flask
import os
from . import dbmethods

app = Flask(__name__)

MONGOHOST = "mongodb://localhost:27017"

try:
	dbmethods.connect(MONGOHOST)
except:
	print("error connecting to Mongo")

from app import routes