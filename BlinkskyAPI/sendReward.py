import requests
import json
from pprint import pprint
from FirebaseCredentials.Firebase import db
import datetime
url = "https://api.blinksky.com/api/v1/send"

def SendReward(company,adminPhone,emp_phone,amount,employee_id,employee_name,admin_id):
  payload = json.dumps({
     "gift": {
       "action": "order",
       "apikey": "62635cf197d1476bbb3d908c81a4645b",
       "sender": company,
       "from": adminPhone,
       "dest": emp_phone,
       "code": "62",
       "amount": amount,
       "postal": "30005",
       "msg": "Well Done",
       "reference": "Best Work",
       "handle_delivery": False
     }
   })
  headers = {
  'Content-Type': 'application/json',
 }

  response = requests.request("POST", url, headers=headers, data=payload)
  result=json.loads(response.content)
  redeeminglink=result['d']['list'][0]['reference']
  id=result['d']['list'][0]['sessionid']
  current_time = datetime.datetime.now() 
  employee_id=employee_id.upper()
  data={
        "action":"Issued to "+employee_name,
        "CardValue":amount,
        "date": str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year),
    }
  db.child("Users").child(admin_id).child("rewards").child(id).set(data)
  data={
        "link": redeeminglink,
        "value":amount,
        "date": str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year),
    }
  db.child("Users").child(employee_id).child("rewards").child(id).set(data)
  return redeeminglink
