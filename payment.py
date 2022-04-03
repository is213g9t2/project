from flask import Flask, jsonify, redirect, render_template, request, render_template
from flask_cors import CORS
import json
import amqp_setup
import pika
from invokes import invoke_http
# from sms import sms
import firebase_admin
import os
from makePayment import make_payment
# from twilio.rest import Client

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


getPolicies = db.reference("/Policy")
policydata = getPolicies.get()




outstandingpolicy= ''
@app.route("/getpayment/<string:amt>/<string:customerID>", methods=['POST'])
def payment(amt,customerID):
    amt = 0
    outstandingpolicy= ''
    getCustomerRef = db.reference("/customer/"+customerID)
    data1 = getCustomerRef.get()
    getCustPolicies = db.reference("/Policy/")
    custdata1 = getCustPolicies.get()
    print(custdata1)
    for (i,m) in custdata1.items():
        for (e,j) in data1.items():
            for k in j:
                if i == k:
                    dict[i] = m
                    if m['PaymentStatus'] == "Outstanding":
                        amt = m["Price"]
                        outstandingpolicy = i
                        print(outstandingpolicy)
    make_payment(customerID)
    hopper_ref = policy_ref.child(outstandingpolicy)
    hopper_ref.update({
            "PaymentStatus": "Paid",
            "PaymentDate":dateee,
            "OutstandingAmt": '0',
            "Status":"Active"
    })
    # sms()
    
    return jsonify(
        {
            "data": amt
        }
    ), 201

dict={}

@app.route('/getDetails/<string:customerID>')
def getDetails(customerID):
    getPolicy = "http://localhost:5001/getPolicy/" + customerID
    policy = invoke_http(getPolicy)
    amt = 0
    outstandingpolicy = ''
    for i in policy:
        getCustPolicies = db.reference("/Policy/")
        custdata1 = getCustPolicies.get()
        for e in policy['data']:
                for (i,m) in custdata1.items():
                    if i == e:
                        dict[e] = m
                        if m['PaymentStatus'] == "Outstanding":
                            amt = m["Price"]
                            outstandingpolicy = i
    print(outstandingpolicy)
    return  jsonify(
            {
                "code": 200,
                "data": dict,
                "amt":amt,
                "policykey": outstandingpolicy
            }       
    )
# amt = 0
# outstandingpolicy = ''
# custID = '113538498334279602821'
# getCustomerRef = db.reference("/customer/113538498334279602821")
# data = getCustomerRef.get()

# getCustPolicies = db.reference("/Policy/")
# custdata = getCustPolicies.get()

# for (i,m) in custdata.items():
#     for (e,j) in data.items():
#         for k in j:
#             if i == k:
#                 if m['PaymentStatus'] == "Outstanding":
#                     amt = m["Price"]
#                     outstandingpolicy = k
# print(outstandingpolicy)
# print(amt)
# policy1 = policydata
                                                                              
# amt = 0
# outstandingpolicy = ''
# for (x,y) in policy1.items():
#     if y['PaymentStatus'] == "Outstanding":
#         amt = y["Price"]
#         outstandingpolicy = x
# print(amt)
# print(outstandingpolicy)
# print(policy1[outstandingpolicy])
    # if policy["PaymentStatus"] == "Outstanding":
    #     amt = policy["Price"]

    # elif policy["PaymentStatus"] == "Paid":
    #     amt = policy["OutstandingAmt"]
    # print(amt)

# @app.route('/display')
# def display():
#     getPoliciesLate = db.reference("/Policy")
#     policy1data = getPoliciesLate.get()
#     for (i,m) in custdata.items():
#         for (e,j) in data.items():
#             for k in j:
#                 if i == k:
#                     print(k)
    
#     return  jsonify(
#             {
#                 "code": 200,
#                 "data": policy1data
#             }       
#     )
    
<<<<<<< Updated upstream
# dict = {}
# @app.route('/display/<string:customerID>')
# def display(customerID):
#     amt = 0
#     getCustomerRef = db.reference("/customer/"+customerID)
#     data1 = getCustomerRef.get()
#     getCustPolicies = db.reference("/Policy/")
#     custdata1 = getCustPolicies.get()
#     for (i,m) in custdata1.items():
#         for (e,j) in data1.items():
#             for k in j:
#                 if i == k:
#                     dict[i] = m
#                     if m['PaymentStatus'] == "Outstanding":
#                         amt = m["Price"]
#                         print(amt)
#     return  jsonify(
#             {
#                 "code": 200,
#                 "data": dict,
#                 "amt": amt
#             }       
#     )
=======
dict = {}
@app.route('/display/<string:customerID>')
def display(customerID):
    amt = 0
    getCustomerRef = db.reference("/customer/"+customerID)
    data1 = getCustomerRef.get()
    getCustPolicies = db.reference("/Policy/")
    custdata1 = getCustPolicies.get()
    for (i,m) in custdata1.items():
        for (e,j) in data1.items():
            for k in j:
                if i == k:
                    dict[i] = m
                    if m['PaymentStatus'] == "Outstanding":
                        amt = m["Price"]
    return  jsonify(
            {
                "code": 200,
                "data": dict,
                "amt": amt
            }       
    )

outstandingpolicy= ''
@app.route("/getpayment/<string:amt>/<string:customerID>", methods=['POST'])
def payment(amt,customerID):
    amt = 0
    outstandingpolicy= ''
    getCustomerRef = db.reference("/customer/"+customerID)
    data1 = getCustomerRef.get()
    getCustPolicies = db.reference("/Policy/")
    custdata1 = getCustPolicies.get()
    print(custdata1)
    for (i,m) in custdata1.items():
        for (e,j) in data1.items():
            for k in j:
                if i == k:
                    dict[i] = m
                    if m['PaymentStatus'] == "Outstanding":
                        amt = m["Price"]
                        outstandingpolicy = i
                        print(outstandingpolicy)
    make_payment(customerID)
    hopper_ref = policy_ref.child(outstandingpolicy)
    hopper_ref.update({
            "PaymentStatus": "Paid",
            "PaymentDate":dateee,
            "OutstandingAmt": '0',
            "Status":"Active"
    })
    # sms()
    
    return jsonify(
        {
            "data": amt
        }
    ), 201
# paymenturl = "http://localhost:5001/make_payment"

# test = invoke_http(paymenturl, json=policy1)
# print("hi",test)

# make_payment()
>>>>>>> Stashed changes

# @app.route('/getAmount')
# def getAmt():
#     getPoliciesLate = db.reference("/Policy")
#     policy1data = getPoliciesLate.get()
#     amt = 0
#     for (x,y) in policy1data.items():
#         print(x,y)
#         if y['PaymentStatus'] == "Outstanding":
#             amt = y["Price"]
#     return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "Amt":amt,
#                     "details":policy1,
#                     "policykey":outstandingpolicy
#                 }
#             }
#         )

<<<<<<< Updated upstream
# dict1 = {}
# @app.route('/getAmount/<string:customerID>')
# def getAmt(customerID):
#     amt = 0
#     outstandingpolicy = ''
#     getCustomerRef = db.reference("/customer/"+customerID + "/")
#     data1 = getCustomerRef.get()
#     getCustPolicies = db.reference("/Policy/")
#     custdata1 = getCustPolicies.get()
#     for (i,m) in custdata1.items():
#         for (e,j) in data1.items():
#                 for k in j:
#                     if i == k:
#                         dict1[i] = m
#                         if m['PaymentStatus'] == "Outstanding":
#                             amt = m["Price"]
#                             outstandingpolicy = i
#                             print(outstandingpolicy)
#                             print(amt)
#     return jsonify(
=======
dict1 = {}
@app.route('/getAmount/<string:customerID>')
def getAmt(customerID):
    amt = 0
    outstandingpolicy = ''
    getCustomerRef = db.reference("/customer/"+customerID + "/")
    data1 = getCustomerRef.get()
    getCustPolicies = db.reference("/Policy/")
    custdata1 = getCustPolicies.get()
    for (i,m) in custdata1.items():
        for (e,j) in data1.items():
                for k in j:
                    if i == k:
                        dict1[i] = m
                        if m['PaymentStatus'] == "Outstanding":
                            amt = m["Price"]
                            outstandingpolicy = i
                            print(outstandingpolicy)
        
        return jsonify(
                {
                    "code": 200,
                    "data": {
                        "Amt":amt,
                        "data":dict1,
                        "policykey":i
                    }
                }
            )

# @app.route('/getDetails')
# def getDetails():
#     return  jsonify(
>>>>>>> Stashed changes
#             {
#                 "code": 200,
#                 "data": {
#                     "Amt":amt,
#                     "data":dict1,
#                     "policykey":i
#                 }
#             }
#         )



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5501',debug=True)