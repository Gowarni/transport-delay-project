import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# 🔹 Load dataset
df = pd.read_csv("data/dataset.csv")

print("Dataset Loaded:\n", df.head())

# 🔹 Features (X) and Target (y)
X = df[['temperature', 'humidity', 'hour', 'day']]
y = df['delay']

# 🔹 Train model
model = RandomForestRegressor()
model.fit(X, y)

print("\nModel trained successfully!")

# 🔹 Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved as model.pkl")