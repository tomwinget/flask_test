from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient()

db = client['ip_database']
collection = db['current_collection']


@app.route('/')
def hello_world():
	data = collection.find({})
	return render_template('index.html', data=data)
