import requests
print('reqfile version: ', requests.__version__)

req_call_back = requests.get("https://raw.githubusercontent.com/Leroy777/CMPUT-404-Lab-1/script.py")
print(req_call_back.content)
