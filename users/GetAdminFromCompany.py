from FirebaseCredentials.Firebase import db


def CompanyAdmins(company):
    company=company.upper()
    all_employees=db.child("Users").get()
    a=[]
    for employee in all_employees.each():
        employee_id=employee.key()
        path="Users/"+employee_id+"/profile/company"
        employee_company=db.child(path).get().val()
        if(employee_company==company):
            if db.child("Users/"+employee_id+"/profile/status").get().val()=="admin":
             a.append(employee_id)
    return a 
