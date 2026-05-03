import pickle
from datetime import datetime

from weather import get_weather
from train_api import get_train_data


# 🔹 Load trained model
model = pickle.load(open("model.pkl", "rb"))


def predict_delay(city, station):
    
    # 🔹 Get real-time data
    temp, humidity = get_weather(city)
    train_data = get_train_data(station)

    # 🔹 Time features
    now = datetime.now()
    hour = now.hour
    day = now.weekday()

    print("\n--- INPUT DATA ---")
    print("Temperature:", temp)
    print("Humidity:", humidity)
    print("Hour:", hour)
    print("Day:", day)

    # 🔹 Prepare input for model
    features = [[temp, humidity, hour, day]]

    # 🔹 Predict delay
    prediction = model.predict(features)[0]

    print("\n🚆 Predicted Delay:", round(prediction, 2), "minutes")


# 🔥 TEST
if __name__ == "__main__":
    predict_delay("Hyderabad", "NDLS")