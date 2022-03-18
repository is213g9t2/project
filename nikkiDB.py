import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
  'databaseURL':'https://esdg9t02-insurance-default-rtdb.asia-southeast1.firebasedatabase.app/'
  })

from firebase_admin import db

ref = db.reference("/")
customer_ref = ref.child('customer')

hopper_ref = customer_ref.child('123')
hopper_ref.update({
        "paymentStatus": "paid",
        "amount": "123"
})