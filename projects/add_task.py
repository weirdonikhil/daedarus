from FirebaseCredentials.Firebase import db

def Create_task(task_name,task_id,project_task_id,task_description,employee_id):
 project_id=project_task_id
 data={
     "name":task_name,
     "id":task_id,
     "description":task_description
    }
 db.child("Users").child(employee_id).child("Projects").child(project_id).child("tasks").child(task_id).set(data)
 