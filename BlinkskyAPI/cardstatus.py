import requests
import json
from pprint import pprint

url = "https://api.blinksky.com/api/v1/status"

payload = json.dumps({
 "service": {
      "apikey": "62635cf197d1476bbb3d908c81a4645b",
      "sessionid": "834d973173f3412aaf912a75d3d88672"
    }
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

pprint(json.loads(response.content))