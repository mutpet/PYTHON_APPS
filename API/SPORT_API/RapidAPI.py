
"""_summary_
A regisztációhoz kötött, de ingyenes 'API' szolgáltatásokat (RapidAPI -it) használó példa, gyakorló python alkalmazás.
_URL_: https://rapidapi.com/weatherapi/api/weatherapi-com/
Python 3.x Kompatibilis
_Created by_: Mutter Péter    
"""

#python pip install --upgrade
#python -m pip install requests

#modulok:
from requests import Session
import requests
from requests import get
import secrets
import json
#import pprint
from pprint import pprint as pp

#Alap GET request tesztelése:
#print(response.status_code)
base_url = "https://weatherapi-com.p.rapidapi.com"
endpoint_tag = "/sports.json"
url = base_url + endpoint_tag
querystring = {"q":"Budapest"}
headers = {
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    "X-RapidAPI-Key": secrets.API_KEY,
    #"X-RapidAPI-Key": "82b07d85b9mshb5857f10c10be1bp19038djsn35c501e359f8"
}
#response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.get(url, headers=headers, params=querystring)

#Lekért, visszakapott eredmény kiiratásai:

#Szövegként:
#print(response.text)

#json formátumban:
#print(response.json())

#áttekinthető, rendezett json fromában:
#result = json.loads(response.text)
#pp(result)

#csak bizonyos kulcsú értékeket jelenítsünk meg a json fromátumból
"""
data = response.json()

for item in data['football']:
  print(item['match'])
"""

#Készítsünk, egy általános Osztályt az API lekérésekhez:
"""_summary_
    Alaposztály. Osztályváltozók beállítása. Alapbeállítások az ingyenes RapidAPI - WeatherAPI.com szolgáltatás használatához.
    Returns:
        avoid: API Get-header, és API URL beállítása.       
"""

class SetApiRequest:
    def __init__(self, token):
        self.base_url = "https://weatherapi-com.p.rapidapi.com"
        #self.apiurl = base_url + endpoint_url
        self.headers = {"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com", "X-RapidAPI-Key": token,}
        #self.params = {"q":"Budapest"}
        self.session = Session()
        self.session.headers.update(self.headers)

        """_summary_
           Metódus. API-in lekéri JSON formátumban, a megrendezésre kerülő futball meccseket.
           Returns:
               JSON:data (futball meccsek adatai.)
        """
    def getFootballEvents(self, params):
        url = self.base_url + "/sports.json"
        response = self.session.get(url, params = params)
        data = response.json()['football']
        #result= json.loads(response.text)
        return pp(data)

        """_summary_
           Metódus. API-in lekéri JSON formátumban, megadott városnév alapján az időjárási adatokat.
           Returns:
               JSON:temp (megadott város időjárás adatai.)
        """        
    def getCurrentTemp(self, params):
        url = self.base_url + "/current.json"
        response = self.session.get(url, params = params)
        data = response.json()['current']['temp_c']
        temp = print(f"Budapesten a jelenlegi hőmérséklet {int(data)} C° fok.")
        return temp

        """_summary_
        """
    def getIpAddress(self):
        #Egy másik ingyenes IP lekérő API -in lekérjük az aktuális publikus IP címünket, sztringként.
        ip = get('https://api.ipify.org').text
        url = self.base_url + "/ip.json"
        response = self.session.get(url, params = {"q": ip})
        result= json.loads(response.text)
        return pp(result)

set_api = SetApiRequest(secrets.API_KEY)

#Futball események lekérdezése:
set_api.getFootballEvents({"q":"Budapest"})

#Aktuális, budapest hőmérséklet lekérdezése:
print(set_api.getCurrentTemp({"q":"Budapest"}))

#Adott eszköz, aktuális, publikus IP címének és adatainak lekérése:
set_api.getIpAddress()