from FirebaseCredentials.Firebase import db

def submission_details(employee_id):
    task_details=db.child("Users/"+employee_id+"/task_submissions").get()
    a=[]
    for task in task_details.each():
      a.append(task.val())
    return a


