import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})

from firebase_admin import db

ref = db.reference("/")

import json
with open("customer.json", "r") as f:
	file_contents = json.load(f)
ref.update(file_contents)


# increment_customer = "customer_test"

# # to write new table header
# customer_ref = ref.child('customer')
# customer_ref.set({
#     'customerID': {
#         'Password': 'Password',
#         'Name': 'Name',
#         'Gender': 'Gender',
#         'Dob': 'Dob',
#         'EmailAddress': 'EmailAddress',
#         'MobileNumber': 'MobileNumber',
#         'MedicalConditions': 'MedicalConditions',
#         'UploadDocument': 'UploadDocument'
#     },

#     increment_customer: {
#         'Password': 'Password',
#         'Name': 'Name',
#         'Gender': 'Gender',
#         'Dob': 'Dob',
#         'EmailAddress': 'EmailAddress',
#         'MobileNumber': 'MobileNumber',
#         'MedicalConditions': 'MedicalConditions',
#         'UploadDocument': 'UploadDocument'
#     }
# })


# # to update table header
# hopper_ref = customer_ref.child('customer')
# hopper_ref.update({
#         'Password': 'Password',
#         'Name': 'Name',
#         'Gender': 'Gender',
#         'Dob': 'Dob',
#         'EmailAddress': 'EmailAddress',
#         'MobileNumber': 'MobileNumber',
#         'MedicalConditions': 'MedicalConditions',
#         'UploadDocument': 'UploadDocument'
# })



increment_catalogue = "catalogue_test"

catalogue_ref = ref.child('catalogue')
catalogue_ref.set({
    
    increment_catalogue: {
        'PolicyID': 'PolicyID',
        'PlanDesc': 'PlanDesc ',
        'Country': 'Country',
        'Price' : 'Price'

    }
})


hopper2_ref = catalogue_ref.child('catalogue2')
hopper2_ref.update({
        'PolicyID': 'PolicyID',
        'PlanDesc': 'PlanDesc ',
        'Country': 'Country',
        'Price' : 'Price'
})


