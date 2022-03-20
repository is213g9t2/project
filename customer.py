import tempfile
import firebase_admin
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})

from firebase_admin import db

ref = db.reference("/")

# Customer creates new account
@app.route("/customer/<string:details>", methods=['POST'])
def customer(details):
    print(details)
    dictionary = json.loads(details)

    # Writes new account details to customer.json
    def write_json(details, filename="customer.json"):
        with open (filename, "r+") as datafile:
            data = json.load(datafile)
            data['customer']["1000"] = dictionary
            datafile.seek(0)
            json.dump(data, datafile, indent=4)

    write_json(details)

    return jsonify(
        {
            "data": details
        }
    ), 201

# Reads customer.json and publishes on Firebase
with open("customer.json", "r") as f:
    file_contents = json.load(f)
ref.set(file_contents)

if __name__ == "__main__":
    app.run(port='5500',debug=True)