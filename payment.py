from unittest import result
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json

import firebase_admin


app = Flask(__name__)
CORS(app)

cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
  'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
  })

from firebase_admin import db

ref = db.reference("/")
customer_ref = ref.child('customer')



@app.route("/getpayment/<string:amt>", methods=['POST'])
def payment(amt):
    amt = request.get_json()
    result = json.loads(amt)
    for i in result:
        finalamt = result[i]
    print(finalamt)
    
    
    hopper_ref = customer_ref.child('customerID')
    hopper_ref.update({
            "paymentStatus": "paid",
            "amount": finalamt
    })
    
    print(type(result))

    return jsonify(
        {
            "data": amt
        }
    ), 201







if __name__ == "__main__":
    app.run(port='5500',debug=True)