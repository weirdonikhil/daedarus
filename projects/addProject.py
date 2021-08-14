from FirebaseCredentials.Firebase import db

def CreateProject(project_name,project_id,members,project_description,employee_id):
    project_members=members.split(',')
    project_details={
        "name":project_name,
        "id":project_id,
        "members":project_members,
        "description":project_description,
    }
    db.child("Users").child(employee_id).child("Projects").child(project_id).set(project_details)
    for project_member in project_members:
        emp_id=project_member
        db.child("Users").child(emp_id).child("Projects").child(project_id).set(project_details)
        