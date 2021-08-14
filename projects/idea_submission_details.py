from FirebaseCredentials.Firebase import db

def business_idea(employee_id):
    idea_details=db.child("Users/"+employee_id+"/ideaSubmission").get()
    a=[]
    for task in idea_details.each():
      a.append(task.val())
    return a