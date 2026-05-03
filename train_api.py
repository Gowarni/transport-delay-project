import requests

API_KEY = "0cdcd2dbe1mshd8bcb040d424279p14083fjsnb5e6c6b0f68c"

def get_train_data(station_code):
    url = "https://irctc1.p.rapidapi.com/api/v3/getLiveStation"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
    }

    params = {
        "fromStationCode": station_code,
        "hours": 1   # ✅ use INTEGER not string
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    print("API Response:", data)

    return data


# 🔥 TEST
if __name__ == "__main__":
    station = "NDLS"   # try NDLS first

    result = get_train_data(station)

    print("\nTrain Data Received Successfully!")