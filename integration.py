import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("final_model.pkl", "rb"))
df = pd.read_csv("data/etrain_delays (1).csv")


def predict_delay(from_station, to_station, day_of_week):

    try:
        station_data = df[df['station_code'] == from_station.upper()]

        if station_data.empty:
            return None

        results = []

        for _, row in station_data.head(3).iterrows():

            features = np.array([[
                row['pct_right_time'],
                row['pct_slight_delay'],
                row['pct_significant_delay'],
                row['pct_cancelled_unknown'],
                day_of_week
            ]])

            prediction = model.predict(features)[0]

            confidence = max(50, min(99, round(100 - abs(prediction)*2, 2)))

            results.append({
                "train_name": row['train_name'],
                "train_number": row['train_number'],
                "delay": round(prediction, 2),
                "confidence": confidence
            })

        return results

    except Exception as e:
        print("Error:", e)
        return None