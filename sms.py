import os
from flask import Flask
from flask_cors import CORS
from twilio.rest import Client
import firebase_admin
app = Flask(__name__)
CORS(app)
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
  'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
  })

def sms():

    getPoliciesLate = db.reference("/Policy")
    policy1data = getPoliciesLate.get()
    for (x,y) in policy1data.items():
        print(x,y)
        # amt = 0
        outstandingpolicy = ''
        if y['PaymentStatus'] == "Outstanding":
            outstandingpolicy = x
            # amt = y["Price"]


    account_sid = 'AC539b44c37c8c2ba35a30d26bc9aa535c'
    auth_token = 'f32b0573cae9369d7ee380feb12ff5fa'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=outstandingpolicy + "Coverage from: paid",
            # need to configure
            from_='+15739833775',
            to='+6590696280'
        )

    print(message.sid)