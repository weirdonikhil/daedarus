from FirebaseCredentials.Firebase import db

def admin_ID(admin_email):
    all_employees=db.child("Users").get()
    for employee in all_employees.each():
        employee_id=employee.key()
        path="Users/"+employee_id+"/profile/email"
        employee_email=db.child(path).get().val()
        if(employee_email==admin_email):
            adminId=employee_id
            break
    return adminId

