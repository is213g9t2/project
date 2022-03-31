from flask import Flask, jsonify, redirect, render_template, request, render_template
from flask_cors import CORS
import json
import amqp_setup
import pika
from invokes import invoke_http
import firebase_admin
app = Flask(__name__)

CORS(app)
cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
  'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
  })

from firebase_admin import db
import datetime

dateee = datetime.datetime.now().date()
dateee = dateee.strftime("%m-%d-%Y")

ref = db.reference("/")
customer_ref = ref.child('customer')
policy_ref = ref.child('Policy')

getCustomerRef = db.reference("/customer/customerID")
data = getCustomerRef.get()

getPolicies = db.reference("/Policy")
policydata = getPolicies.get()


# policy = policydata["123Africa0103-31-2022"]
policy1 = policydata
print(policy1)

amt = ''
outstandingpolicy = ''
for (x,y) in policy1.items():
    print(x,y)
    if y['PaymentStatus'] == "Outstanding":
        amt = y["Price"]
        outstandingpolicy = x
    elif y['PaymentStatus'] == "Paid":
        amt = y["OutstandingAmt"]
print(outstandingpolicy)
    # if policy["PaymentStatus"] == "Outstanding":
    #     amt = policy["Price"]

    # elif policy["PaymentStatus"] == "Paid":
    #     amt = policy["OutstandingAmt"]
    # print(amt)
@app.route('/display')
def display():
    getPoliciesLate = db.reference("/Policy")
    policy1data = getPoliciesLate.get()
    
    return  jsonify(
            {
                "code": 200,
                "data": policy1data
            }       
    )

@app.route("/getpayment/<string:amt>", methods=['POST'])
def payment(amt):
    print(amt)
    hopper_ref = policy_ref.child(outstandingpolicy)
    hopper_ref.update({
            "PaymentStatus": "Paid",
            "PaymentDate":dateee,
            "OutstandingAmt": 0,
            "Status":"Active"
    })
    return jsonify(
        {
            "data": amt
        }
    ), 201

@app.route('/getAmount')
def getAmt():
    getPoliciesLate = db.reference("/Policy")
    policy1data = getPoliciesLate.get()
    for (x,y) in policy1data.items():
        print(x,y)
        if y['PaymentStatus'] == "Outstanding":
            amt = y["Price"]
        elif y['PaymentStatus'] == "Paid":
            amt = y["OutstandingAmt"]

    return jsonify(
            {
                "code": 200,
                "data": {
                    "Amt":amt,
                    "details":policy1
                }
            }
        )

@app.route('/getDetails')
def getDetails():
    
    return  jsonify(
            {
                "code": 200,
                "data": policy1
            }       
    )
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5501',debug=True)