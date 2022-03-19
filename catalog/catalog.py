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


# db = ???(app)

ref = db.reference("/")


#Get all available policies
@app.route("/catalog")
def get_all():
    catalog = request.get_json()
    result = json.loads(catalog)

    if len(result):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "catalog": [result.json() for region in catalog]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no policies available."
        }
    ), 404