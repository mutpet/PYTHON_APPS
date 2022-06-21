"""
ZEEP SOAP KLIENS ALAP PÉLDA:
import zeep
wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))
"""
#pip install zeep
#pip install lxml
from zeep import Client
from datetime import datetime
from bs4 import BeautifulSoup

current_date = datetime.today().strftime('%Y-%m-%d')
#wsdl_url = "http://www.mnb.hu/arfolyamok.asmx?wsdl"
#soap_client = Client(wsdl_url)


def MNBSoapRequest(start_date_usr_input, end_date_usr_input, rateCurrency):
 wsdl_url = "http://www.mnb.hu/arfolyamok.asmx?wsdl"
 soap_client = Client(wsdl_url)
 mnb_soap_result = soap_client.service.GetExchangeRates(start_date_usr_input, end_date_usr_input, rateCurrency)     
 soup = BeautifulSoup(mnb_soap_result, 'xml')
 #for i in soup.find_all('Rate'):
 for i in soup.find_all('Day'):
   rate = i
   #rate = i.text 
   print(f"\x1b[6;30;42m MNB hivatalos napi devizaárfolyam:\x1b[0m \x1b[5;30;47m {rate} \x1b[0m")

#mnb_api_result = soap_client.service.GetCurrentExchangeRates()
#mnb_soap_result = soap_client.service.GetExchangeRates(current_date, current_date, 'EUR,USD')

"""
with open('mnb_eur_usd_napi_arfolyam.xml', 'w') as f:
        f.write(mnb_api_result)
"""
#print(mnb_soap_result + "\n")

""""
#rate = str()
soup = BeautifulSoup(mnb_soap_result, 'xml')
for i in soup.find_all('Rate'):
 rate = i
 #rate = i.text 
 print(rate)
"""

def UserIntervalValidation(start_date_usr_input, end_date_usr_input):
 format = '%Y-%m-%d'
 rateCurrency = 'EUR,USD'
 check_date_format = True
 try:
    check_date_format = bool(datetime.strptime(start_date_usr_input, format))
 except ValueError:
    check_date_format = False
    print(f'Hiba történt a beviteli érték dátumértékké való átkonvertálásakor! Kérlek ellenőrizd a bevitt értékeket! Kezdő dátumérték: {start_date_usr_input} Befejezeő dátumérték: {end_date_usr_input}')     
 if start_date_usr_input != '' and end_date_usr_input != '' and check_date_format == True:    
         start_date = datetime.strptime(start_date_usr_input, format)
         end_date =  datetime.strptime(end_date_usr_input, format)
         MNBSoapRequest(start_date_usr_input, end_date_usr_input, rateCurrency)
 else: print("Nem megfelelő dátumértéket adtál meg!\nKezdeti dátumérték: " + str(start_date_usr_input) + "\nBefejező dátumérték: " + str(end_date_usr_input) + "\nKérlek ellnőrizd és próbáld meg újra!")

start_date_usr_input = input("Kérlek add meg a devizaárfolyam kezdeti dátumát (Év-hónap-nap formátumban)!\n")
end_date_usr_input = input("Kérlek add meg a devizaárfolyam befejező dátumát (Év-hónap-nap formátumban)!\n")
UserIntervalValidation(start_date_usr_input, end_date_usr_input)