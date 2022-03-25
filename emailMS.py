from venv import create
from gmailAPI import create_message, main

import json
import os

import amqp_setup

monitorBindingKey='#.invoice'

def receiveEmailRequest():
    amqp_setup.check_setup()
        
    queue_name = 'Invoice'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an email request by " + __file__)
    processEmailRequest(json.loads(body))
    print() # print a new line feed

def processEmailRequest(EmailReq):
    print("Recording an email request:")

    emailObject = create_message("esdg9t02@gmail.com", EmailReq.recipient, EmailReq.subject, EmailReq.message)
    ## emailObject = create_message("esdg9t02@gmail.com", "hengweishin@gmail.com", "testing email subject", "hello world content")

    status = main(emailObject)

    return status
    

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveEmailRequest()


