import requests
import os
cookie = os.environ.get("cookie")
formkey = os.environ.get("formkey")
url = "http://localhost:3000/chat/a2"

x = requests.get(url, headers={"Cookie":cookie,"Quora-Formkey":formkey}, params={"message":"hi"})
print(x.json())