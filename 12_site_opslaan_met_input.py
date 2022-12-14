import requests

def load_site():
    url = input("Welke url wil je opslaan?: ")
    bestandsnaam = input("Als welk bestand wil je het opslaan?: ")
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


load_site()
