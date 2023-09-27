import requests
import json
import csv

auth_key = '--API-KEY--'

headers = {'x-apikey': auth_key}
res = requests.get('https://api.bitskins.com/market/skin/730', headers=headers)
response = json.loads(res.text)

if res.status_code == 200:
    with open('bitskins_data.csv', 'w', newline='', encoding='utf-8') as csvfile:  # Hier den Zeichensatz auf UTF-8 setzen
        fieldnames = ['name', 'suggested_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for item in response:
            if item['suggested_price'] is not None:
                suggested_price = round(int(item['suggested_price']) / 1000, 2)  # Teilen, runden und auf 2 Nachkommastellen begrenzen
                writer.writerow({'name': item['name'], 'suggested_price': suggested_price})
    print("CSV-Datei erfolgreich erstellt: bitskins_data.csv")
else:
    print("Fehler bei der Anfrage an die BitSkins API:", res.status_code)
