from FirebaseCredentials.Firebase import auth,db

def employee_login(email,password):
    auth.sign_in_with_email_and_password(email,password)