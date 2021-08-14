from FirebaseCredentials.Firebase import db

def GetRewardDetails(user_id):
    rewards=db.child("Users").child(user_id).child("rewards").get()
    a=[]
    for reward in rewards.each():
        a.append(reward.val())
    return a
