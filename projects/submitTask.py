from projects.getProjectAdmin import get_admin
from FirebaseCredentials.Firebase import db
from pprint import pprint
import datetime
def submit_task(project_name,project_id,task_name,task_id,employee_id):
    current_time = datetime.datetime.now() 
    member_data={
        "project_name":project_name,
        "task_name":task_name,
        "task_id":task_id,
        "date": str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year),
        "status":"Submitted",
        "ratings":"/5",
    }
    db.child("Users").child(employee_id).child("task_submissions").child(task_id).set(member_data)
    admin_data={
        "employee_id":employee_id,
        "name": db.child("Users").child(employee_id).child("profile/name").get().val(),
        "project_name":project_name,
        "ratings":"/5",
        "status":"Submitted",
        "submission_date":str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year),
        "task_id":task_id,
    }
    admin_employee_id=get_admin(project_id)
    db.child("Users").child(admin_employee_id).child("task_submissions").child(task_id).set(admin_data)
