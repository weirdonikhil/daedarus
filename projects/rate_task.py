from FirebaseCredentials.Firebase import db
def rateProject(rating,employee_id,task_id,user_id):
    db.child("Users").child(employee_id).child("task_submissions").child(task_id).update({"ratings":rating+"/5"})
    db.child("Users").child(user_id).child("task_submissions").child(task_id).update({"ratings":rating+"/5"})