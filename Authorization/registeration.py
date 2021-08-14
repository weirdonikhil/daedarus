from FirebaseCredentials.Firebase import auth,db

def register_user(email,password,employee_code,mobile,employee_company,employee_name,admin):
    auth.create_user_with_email_and_password(email,password)
    company=str(employee_company).upper()
    data={
        "name": employee_name,
        "company": company,
        "email": email,
        "emp_code": employee_code,
        "mobile":mobile,
        "status":"Team Member"
    }
    
    db.child("Users").child(company+"_"+employee_code).child("profile").set(data)

    if admin == "True":
       db.child("Users").child(company+"_"+employee_code).child("profile").update({"status":"admin"})
