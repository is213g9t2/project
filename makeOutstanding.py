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


# @app.route("/makeOutstanding")
# def makeOutstanding(customerID):
    
#         getpayment_URL = "http://localhost:5001/disable/"+ customerID
#         response = requests.get(getpayment_URL)
#         json_data = response.json()
#         r = json.dumps(json_data)
#         print(r)

#         try:
#             order = json_data
#             print(order)

#             amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="#", 
#             body=r)

            
#             print('\n------------------------')
#             print('\nresult: ', r)
#             return jsonify(json_data)

#         except Exception as e:
#             # Unexpected error in code
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#             ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
#             print(ex_str)

#             return jsonify({
#                 "code": 500,
#                 "message": "makeoutstanding.py internal error: " + ex_str
#             }), 500


monitorBindingKey='#'

def receiveError():
    amqp_setup.check_setup()
    
    queue_name = "email"  

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an error by " + __file__)
    print(body)
    processError(body)
    print() # print a new line feed

def processError(errorMsg):
    print("Printing the error message:")
    try:
        error = json.loads(errorMsg)
        print("--JSON:", error)
    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", errorMsg)
    print()


    

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for oustanding email...")
    app.run(host="0.0.0.0", port=5560, debug=True)