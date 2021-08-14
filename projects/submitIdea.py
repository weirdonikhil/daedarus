from users.GetAdminFromCompany import CompanyAdmins
from FirebaseCredentials.Firebase import db
import datetime
def submit_idea(employee_id,idea_tagline,business_model_link,business_model,short_description):
    current_time = datetime.datetime.now() 
    data={
        "business_model_link":business_model_link,
        "complete_description":business_model,
        "date": str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year),
        "employee_id":employee_id,
        "idea_tagline":idea_tagline,
        "name": db.child("Users").child(employee_id).child("profile/name").get().val(),
        "short_description":short_description
    }
    employee_company=db.child("Users").child(employee_id).child("profile/company").get().val()
    company_admins=CompanyAdmins(employee_company)
    for admin in company_admins:
        db.child("Users").child(admin).child("ideaSubmission").child(employee_id).set(data)



