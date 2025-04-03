import requests

# API-endpoint (pas aan als nodig)
API_URL = "https://my-json-server.typicode.com/lars-kthy/JSON_API/klassieke_autos"

# API-aanroep
response = requests.get(API_URL)

# Controleer of de API correct reageert
if response.status_code == 200:
    data = response.json()
    print("Data succesvol opgehaald!")
    
    # Print eerste 5 items
    for item in data[:5]:
        print(item)
else:
    print(f"Fout bij ophalen, {response.status_code}")
