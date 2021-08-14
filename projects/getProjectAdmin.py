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


def get_admin(project_id):
   all_users=db.child("Users").get()
   a=[]
   for user in all_users.each():
       employee_id=user.key()
       status=db.child("Users/"+employee_id+"/profile/status").get().val()
       if status == "admin":
           a.append(employee_id)
   for admin in a:
     if  db.child("Users/"+admin+"/Projects").get().val() is not None:  
      projects= db.child("Users/"+admin+"/Projects").get()
      for project in projects.each():
          admin_project_id=project.key()
          
          if admin_project_id==project_id:
              admin_id=admin
              break
   return(admin_id)

