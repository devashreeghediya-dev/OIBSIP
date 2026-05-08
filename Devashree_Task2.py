import requests

API_KEY = "f3ea54ae06474bfd33bd24e3ef3ea43b"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found.")
            return

        print("\n--- Weather Info ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])

    except Exception as e:
        print("Error:", e)


while True:
    city = input("\nEnter city (or 'exit'): ")
    if city.lower() == "exit":
        break
    get_weather(city)
