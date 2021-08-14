import pyrebase

firebase_config={
    "apiKey": "AIzaSyDx6CHLGLryz-iIECPKEtaaJI7tNCg5UHc",
    "authDomain": "blinakathon.firebaseapp.com",
    "databaseURL": "https://blinakathon-default-rtdb.firebaseio.com/",
    "projectId": "blinakathon",
    "storageBucket": "blinakathon.appspot.com",
    "messagingSenderId": "593133696040",
    "appId": "1:593133696040:web:a95d5660a557d347ea311d"
}

firebase=pyrebase.initialize_app(firebase_config)
auth=firebase.auth()
db=firebase.database()
