import requests


#get content
response=requests.get("https://www.github.com")
content=response.text
print(content)
#content=response.content
#print(type(content))
with open ("github.html","w") as file:
    file.write(content)
#Encoding
response.encoding="utf-8"
print(response.encoding)


