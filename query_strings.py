import requests
#Simple query strings
params={
    "search_query":"python",
}
response=requests.get("https://www.youtube.com/results",params=params)
print(response.encoding)
print(response.status_code)
content=response.content
with open("search.html","wb") as f:
    f.write(content)



