import requests
import json
from pprint import pprint

url = "https://api.blinksky.com/api/v1/redeem"

payload = json.dumps({
 "gift": {
      "apikey": "62635cf197d1476bbb3d908c81a4645b",
      "code": "5304613045812170",
      "pin": "7517",
      "agent": "nikhilpal9111.blinkathon.com",
      "reference": "a225fdbbbb5443f687b5165fb52aa92a",
      "amount": 10
    }
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

pprint(json.loads(response.content))