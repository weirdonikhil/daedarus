from users.GetAdminIdFromEmail import admin_ID
from FirebaseCredentials.Firebase import db
def sendmessage(msg_description,gift_card_value,admin_email,user_id):

    message={
        "body": msg_description,
        "gift_card_value":gift_card_value,
        "from": db.child("Users").child(user_id).child("profile/name").get().val(),
        "emp_id": db.child("Users").child(user_id).child("profile/email").get().val()
    }
    admin_id= admin_ID(admin_email)
    db.child("Users").child(admin_id).child("messages").push(message)
