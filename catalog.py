import os
from flask import Flask, request, jsonify
from flask_cors import CORS

import firebase_admin
from firebase_admin import db


from datetime import datetime
import json
from os import environ


app = Flask(__name__)
CORS(app)
cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})



ref = db.reference("/") 


#Get all available policies
@app.route("/catalog", methods=['GET'])
def get_all():
    catalog = open("catalog.json")
    result = json.load(catalog)

    return result,200


import json
with open("catalog.json", "r") as f:
	file_contents = json.load(f)
ref.update(file_contents)




if __name__ == "__main__":
    app.run(port='5501',debug=True)