import requests
import json
#Json
response=requests.get("https://jajoul.me/wp-content/uploads/2024/11/random-json-data.json")
print(response.status_code)
content=response.json()
print(content)
with open ("sample.json","w") as f:
    json.dump(content[0],f)
#sample file : https://jajoul.me/wp-content/uploads/2024/11/random-json-data.json
