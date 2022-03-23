import os, sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json

import requests

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)


from cgi import print_directory
import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})

from firebase_admin import db

# customerID to be gotten from payment complex microservice
ref = db.reference("/customer/customerID")
data = ref.get()


policy = data["Policies"]
for g, x in policy.items():
    print(x)
    if x["paymentStatus"] == "Outstanding":
        print(x["amount"])
        unpaid = x["amount"]
    

@app.route("/activePolicies")
def get_all():
    if unpaid:
        message = "U BAD, NO GOOD"
        code = 404

    if code not in range(200, 300):

        # Inform nikki's rabbitmq
        # routing key to be determined

        #print('\n\n-----Invoking error microservice as order fails-----')
        print('\n\n-----Publishing the (order error) message with routing_key=#.policies-----')

        # invoke_http(error_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="#.policies", 
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
    


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5001, debug=True)




