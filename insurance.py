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
data = ref.get()
print(data)

# New insurance record created 
@app.route("/catalog", methods=['GET'])
def create_insurance():

    catalog = open("catalog.json")
    result = json.load(catalog)

    return result





#@CALISTA: i think to do this, the json file need to have something. else it wont work. or else u just push into db?
# @app.route("/activepolicies/<string:details>", methods=['POST'])
# def activepolicies(details):
    
#     details = request.get_json()
#     result = json.loads(details)
#     print(type(details))

#     def write_json(details, filename="activepolicies.json"):
#         with open (filename, "r+") as datafile:
#             data = json.load(datafile)
#             dictionary = json.loads(details)
#             print(dictionary)
#             # data['activepolicies']["001"] = dictionary
#             # datafile.seek(0)
#             json.dump(data, datafile, indent=4)

#     write_json(details)

#     return jsonify(
#         {
#             "data": details
#         }
#     ), 201

 



# Reads activepolicies.json and publishes on Firebase
# with open("activepolicies.json", "r") as f:
#     file_contents = json.load(f)
# ref.update(file_contents)

if __name__ == "__main__":
    app.run(port='5500',debug=True)