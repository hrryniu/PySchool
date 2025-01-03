from http.client import responses

import requests


API_KEY="fca_live_dhtgqHvUzuorT3suApzyyWevHi3RtQAlGNigg4b6"
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES= ["USD", "CAD","EUR","AUD", "CNY"]

def convert_currency(base):
    currencies= ",".join(CURRENCIES) #oddzielamy elementy listy przecinkami, bo taki format jest czytelny dla tego api
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
       response = requests.get(url)  #próbujemy otrzymać odpowiedź
       data = response.json()   #w formacie json
       print(data)
       return data["data"] #zwracamy wynik działania funkcji do listy o nazwie data

    except Exception as e:  #jeśli pojawi się błąd to program zapisze go do zmiennej e i wyświetli go bez crashowania prorgamu
        print(e)
        return None

while True:
    base = input("Enter the base currenty(q for quit): ").upper()  #pobieramy od użytkownika walutę bazową i podciągamy ją do duzych liter
    if base== "Q":
            break


    data= convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():#petla, ktora wyswietli wyniki w ładny sposób
        print(f"{ticker}: {value}")