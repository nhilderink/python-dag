import requests

def load_site(url, bestandsnaam):
    res = requests.get(url)
    print(f"Laden... {url}")
    print("============")

    if res.status_code == 200:
        print(f"De site is geladen")
        print(f"code {res.status_code}")
        
        # Content opslaan in bestand
        fh = open(bestandsnaam, "w")
        fh.writelines(res.text)
        fh.close()

    else:
        print("Er ging iets verkeerd")
        print(f"code {res.status_code}")
    
    print(" ")

load_site("http://wietje.bluebit.one.transurl.nl/", "wietje.html")
load_site("http://wietje.bluebit.one.transurl.nl/wiet1.html", "wietje1.html")