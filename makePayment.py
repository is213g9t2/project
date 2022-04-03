from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json
# AMQP service consumer and provider

app = Flask(__name__)
CORS(app)

# def write_json(data, filename="test.json"):
#     with open (filename, "w") as datafile:
#         response = requests.get(getpayment_URL)
#         json_data = response.json()
#         print(json_data)
#         data = json.dumps(json_data)
#         json.dump(data, datafile, indent=4)

# paymenturl = "http://localhost:5001/display"
@app.route("/make_payment")
def make_payment(customerID):
    # with open ("test.json") as json_file:
    #     data = json.load(json_file)
    #     print(data)
    
        getpayment_URL = "http://localhost:5501/getDetails/"+customerID
        response = requests.get(getpayment_URL)
        json_data = response.json()
        r = json.dumps(json_data)

        try:
            order = json_data
            print(order)

            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="123.invoice", 
            body=r)

            
            print('\n------------------------')
            print('\nresult: ', r)
            return jsonify(json_data)

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "makepayment.py internal error: " + ex_str
            }), 500



    

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for making payment...")
    app.run(host="0.0.0.0", port=5500, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
