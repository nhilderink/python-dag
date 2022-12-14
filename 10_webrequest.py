import requests

url = "http://wietje.bluebit.one.transurl.nl/"

res = requests.get(url)

if res.status_code == 200:
    print(f"De site is geladen")
    print(f"code {res.status_code}")
else:
    print("Er ging iets verkeerd")
    print(f"code {res.status_code}")
