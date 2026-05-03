import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    print("Weather API Response:", data)  # Debug

    # ✅ Handle errors properly
    if data.get("cod") != 200:
        print("Error:", data.get("message"))
        return 0, 0   # 👈 instead of None

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return temp, humidity