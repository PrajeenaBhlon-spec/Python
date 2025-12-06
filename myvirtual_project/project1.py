import requests

#r =  requests.get('https://www.w3schools.com/python/module_requests.asp')
response = requests.get("https://catfact.ninja/fact")
"""status = r.status_code

if status == 200:
  print("success")
elif status == 404:
  print("Not found")"""
#print(r)--> provide response
#print(dir(r))

#print(r.text)--> gives a html document of that page

data = response.json()
print(data)