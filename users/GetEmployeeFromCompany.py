from FirebaseCredentials.Firebase import db


def CompanyEmployees(company):
    company=company.upper()
    all_employees=db.child("Users").get()
    a=[]
    for employee in all_employees.each():
        employee_id=employee.key()
        path="Users/"+employee_id+"/profile/company"
        employee_company=db.child(path).get().val()
        if(employee_company==company):
            employee_name=db.child("Users").child(employee_id).child("profile/name").get().val()
            a.append({"name":employee_name,"emp_id":employee_id})
    return a 

