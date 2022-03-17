from firebase_admin import credentials, initialize_app, storage
# Init firebase with your credentials
cred = credentials.Certificate("esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json")
initialize_app(cred, {'storageBucket': 'esdg9t02-insurance.appspot.com'})

# Put your local file path 
fileName = "test.docx"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
# blob.make_public()

print("your file url", blob.public_url)