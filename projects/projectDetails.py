from FirebaseCredentials.Firebase import db

def project_details(employee_id):
    pro_details=db.child("Users/"+employee_id+"/Projects").get()
    a=[]
    for project in pro_details.each():
      a.append(project.val())
    return a

