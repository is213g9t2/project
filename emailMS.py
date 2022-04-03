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

def getPolicyDeets(policykey):

    policy_ref = "/Policy/" + policykey
    policydeets = db.reference(policy_ref).get()

    return policydeets

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

    processEmailRequest(json.loads(body))

    print()  # print a new line feed

    


def processEmailRequest(EmailReq):
    print("Recording an email request:")
    print(EmailReq)
    print()
    
    custdeets = getCustomerDeets(EmailReq["customerID"])
    print(custdeets)
    print()

    policydeets = getPolicyDeets(EmailReq["policykey"])
    print(policydeets)
    print()

    message_text = "Hello " + custdeets["customername"] + "!" + "\n\nThis email is to confirm that we have received your payment of $" + policydeets["Price"]+ " for the Insurance Policy " + policydeets["CatalogID"] + " on " + policydeets["PaymentDate"] + ". \n\nThank you for your purchase!"



    # emailObject = create_message("esdg9t02@gmail.com", custdeets.customeremail, EmailReq.subject, EmailReq.message)
    emailObject = create_message("esdg9t02@gmail.com", custdeets["customeremail"], "Payment Received for [" + policydeets["CatalogID"] + "]", message_text)
    ## emailObject = create_message("esdg9t02@gmail.com", "hengweishin@gmail.com", "testing email subject", "hello world content")

    status = main(emailObject)

    return status


# execute this program only if it is run as a script (not by 'import')
if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveEmailRequest()


# {
#     "amt":"40",
#     "code":200,
#     "data":{
#         "113538498334279602821Africa0104-04-2022":{
#             "CatalogID":"Africa01",
#             "CustID":"113538498334279602821",
#             "OutstandingAmt":"0",
#             "PaymentDate":"04-04-2022",
#             "PaymentStatus":"Paid",
#             "Price":"100",
#             "PurchaseDate":"04-04-2022",
#             "Status":"Active",
#             "phoneNumber":"2022-04-04"
#         },
#         "113538498334279602821Asia0104-04-2022":{
#             "CatalogID":"Asia01",
#             "CustID":"113538498334279602821",
#             "OutstandingAmt":"0",
#             "PaymentDate":"04-04-2022",
#             "PaymentStatus":"Paid",
#             "Price":"20",
#             "PurchaseDate":"04-04-2022",
#             "Status":"Active",
#             "phoneNumber":"2022-04-04"
#         },
#         "113538498334279602821Europe0104-04-2022":{
#             "CatalogID":"Europe01",
#             "CustID":"113538498334279602821",
#             "OutstandingAmt":"40",
#             "PaymentDate":"-",
#             "PaymentStatus":"Outstanding",
#             "Price":"40",
#             "PurchaseDate":"04-04-2022",
#             "Status":"Pending",
#             "phoneNumber":"2022-04-04"
#         }
#     },
#     "policykey":"113538498334279602821Europe0104-04-2022"
# }