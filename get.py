import requests
from requests.exceptions import HTTPError

#simple get method
#response=requests.get("https://www.github.com/ksdjhgksnk")
#Simple Exeptions
""" if response.status_code==200:
    print("OK!")
else:
    print("Not valid!") """
#Exeptions module #nested urls
urls=["https://www.github.com","https://jajoul.me/invalid"]
for url in urls:
    try:
        
        response=requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"Something goes wrong {http_err} with this link {url}")
    except Exception as exp:
        print(f"Something goes wrong.{exp}")
    else:
        print(f"Connected to server of {url}.")

