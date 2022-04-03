from concurrent.futures import process
from venv import create
from gmailAPI import create_message, main

import json
import os

import amqp_setup

## FIREBASE SETUP
import firebase_admin
cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
  'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
  })

from firebase_admin import db

def getCustomerDeets(customerid):

    customer_ref = "/customer/" + customerid
    customeremail = db.reference(customer_ref).child("Email").get()
    customername = db.reference(customer_ref).child("FullName").get()

    custdeets = {
        "customeremail": customeremail,
        "customername": customername ,
        "customerid": customerid
    }

    return custdeets

## MONITOR BINDING KEY
monitorBindingKey = '#.invoice'

def receiveEmailRequest():
    amqp_setup.check_setup()

    queue_name = 'email'

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # an implicit loop waiting to receive messages;
    amqp_setup.channel.start_consuming()
    # it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


# required signature for the callback; no return
def callback(channel, method, properties, body):
    print("\nReceived an email request by " + __file__)
    print("hello")
    print(json.loads(body))
    processEmailRequest(json.loads(body))

    print()  # print a new line feed


def processEmailRequest(EmailReq):
    print("Recording an email request:")

    custdeets = getCustomerDeets(EmailReq["custID"])
    

    # emailObject = create_message("esdg9t02@gmail.com", custdeets.customeremail, EmailReq.subject, EmailReq.message)
    emailObject = create_message("esdg9t02@gmail.com", custdeets["customeremail"], EmailReq["policy"], "hello content")
    ## emailObject = create_message("esdg9t02@gmail.com", "hengweishin@gmail.com", "testing email subject", "hello world content")

    status = main(emailObject)

    return status


# execute this program only if it is run as a script (not by 'import')
if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveEmailRequest()


# EmailReq = {
#     "custID": "123",
#     "policy": "123Africa0104-02-2022" 
# }
# processEmailRequest(EmailReq)

# {
#     "code":200,
#     "data":{
#         "Amt":0,
#         "details":{
#             "123Africa0104-02-2022":{
#                 "CatalogID":"Africa01",
#                 "CustID":"123",
#                 "OutstandingAmt":"50.00",
#                 "PaymentDate":"04-02-2022",
#                 "PaymentStatus":"Outstanding",
#                 "Price":"50.00",
#                 "PurchaseDate":"04-02-2022",
#                 "Status":"Active"
#             },
#             "123America0104-02-2022":{
#                 "CatalogID":"America01",
#                 "CustID":"123",
#                 "OutstandingAmt":"0",
#                 "PaymentDate":"03-01-2020",
#                 "PaymentStatus":"Paid",
#                 "Price":"100.00",
#                 "PurchaseDate":"04-02-2022",
#                 "Status":"Active"
#             },
#             "123Europe0104-02-2022":{
#                 "CatalogID":"Europe01",
#                 "CustID":"123",
#                 "OutstandingAmt":0,
#                 "PaymentDate":"04-02-2022",
#                 "PaymentStatus":"Paid",
#                 "Price":"100.00",
#                 "PurchaseDate":"04-02-2022",
#                 "Status":"Active"
#             }
#         }
#     }
# }