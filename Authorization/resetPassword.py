from FirebaseCredentials.Firebase import auth,db

def reset_password(email):
    auth.send_password_reset_email(email)
    