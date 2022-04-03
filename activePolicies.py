from email import message
from faulthandler import disable
import os, sys
from re import X
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json

import requests

import amqp_setup
import pika
import json

from customer import customer

app = Flask(__name__)
CORS(app)


import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})

from firebase_admin import db

custIDtest = ''

# @app.route("/activePolicies")

def send_message(unpaid):
    code = 404

    if code not in range(200, 300):

        # Inform nikki's rabbitmq
        # routing key to be determined

        #print('\n\n-----Invoking error microservice as order fails-----')
        print('\n\n-----Publishing the (order error) message with routing_key=#.outstanding-----')

        # invoke_http(error_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="#.outstanding", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        # make message persistent within the matching queues until it is received by some receiver 
        # (the matching queues have to exist and be durable and bound to the exchange)

        # - reply from the invocation is not used;
        # continue even if this invocation fails        
        print(str(code) + message + "published to the RabbitMQ Exchange")

        # 7. Return error
        return jsonify(
            {
                "code": code,
                "data": {
                    "unpaid": unpaid
                },
                "message": message
            })

    return



@app.route("/disable/<string:customerID>")
def disable(customerID):
    disabled = "false"
    ref = db.reference("/customer/" + customerID)
    data = ref.get()
    # print(data)
    length = len(data)

    if length != 2:

        ref = db.reference("/customer/" + customerID + "/ActivePolicies")
        data = ref.get()
        disabled = "false"

        for ch in data:
            ref2 = db.reference("/Policy")
            data2 = ref2.get()
            # print(data2)
            for ch2 in data2:
                if ch2 == ch:
                    ref2 = db.reference("/Policy/" + ch2)
                    data2 = ref2.get()
                    policyData = data2["PaymentStatus"]
                    if policyData == "Outstanding":
                        unpaid = data2
                        disabled = "true"
                        send_message(unpaid)
                        break     

    return  jsonify(
        {
            "code": 200,
            "data": disabled
        }       
)



@app.route("/activePolicies/<string:s>", methods=['POST'])
def get_details(s):
    signupdetails = s.split(",")

# customerID to be gotten from payment complex microservice
    ref = db.reference("/customer/customerID")

    # policyID: CustID+CatalogID+PurchaseDate
    # get current data
    import datetime
    x = datetime.datetime.now().date()
    x = x.strftime("%m-%d-%Y")

    customerID = signupdetails[0]
    # customerID = "123"
    
    catalogID = signupdetails[1]
    
    phoneNumber = signupdetails[3]



    ref = db.reference("/Catalog/" + catalogID)
    data = ref.get()
    price = data["price"][1:]

    policyID = customerID + catalogID + x

    ref = db.reference("/customer/" + customerID)
    data = ref.get()
    length = len(data)

    if length == 2:
        ref = db.reference("/")
        data = ref.get()
        customer_ref = ref.child('customer')
        hopper_ref = customer_ref.child(customerID + '/ActivePolicies')
        hopper_ref.update({
                "0": policyID
        })

        policy_ref = ref.child('Policy')
        hopper2_ref = policy_ref.child(policyID)
        hopper2_ref.update({
                'CatalogID': catalogID,
                'CustID': customerID,
                'PurchaseDate': x,
                'PaymentDate' : '-',
                'PaymentStatus': 'Outstanding',
                'Price': price,
                "OutstandingAmt": price,
                "Status":"Pending",
                "phoneNumber": phoneNumber
        })

    else:
        ref = db.reference("/customer/" + customerID + "/ActivePolicies")
        data = ref.get()
        # print(data)
        paid = True
        for ch in data:
            ref2 = db.reference("/Policy")
            data2 = ref2.get()
            for ch2 in data2:
                if ch2 == ch:
                    ref2 = db.reference("/Policy/" + ch2)
                    data2 = ref2.get()
                    policyData = data2["PaymentStatus"]
                    # print(policyData)
                    if policyData == "Outstanding":
                        # print("lol")
                        paid = False
                        break

        if paid == True:
            ref = db.reference("/customer/" + customerID)
            data = ref.get()
            activePolicies = data["ActivePolicies"]
            length = len(activePolicies)
            ref = db.reference("/")
            data = ref.get()
            customer_ref = ref.child('customer')
            hopper_ref = customer_ref.child(customerID + '/ActivePolicies')
            hopper_ref.update({
                    length: policyID
            })

            policy_ref = ref.child('Policy')
            hopper2_ref = policy_ref.child(policyID)
            hopper2_ref.update({
                    'CatalogID': catalogID,
                    'CustID': customerID,
                    'PurchaseDate': x,
                    'PaymentDate' : '-',
                    'PaymentStatus': 'Outstanding',
                    'Price': price,
                    "OutstandingAmt": price,
                    "Status":"Pending",
                    "phoneNumber": phoneNumber
                    
            }) 

@app.route("/getPolicy/<string:customerID>")
def getpolicy(customerID):
    ref = db.reference("/customer/" + customerID + "/ActivePolicies")
    data = ref.get()
    print(data)
    return  jsonify(
        {
            "code": 200,
            "data": data
        }       
    )



if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5001, debug=True)



