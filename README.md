# 🚆 Transport Delay Predictor

## 📌 Project Overview

The **Transport Delay Predictor** is a final-year academic project that leverages Machine Learning techniques to forecast train delays based on historical railway data. The system is designed to assist passengers in estimating potential delays prior to their journey, thereby enabling better travel planning and decision-making.

---

## 🎯 Objective

The primary objective of this project is to develop an intelligent and user-friendly system that:

* Accurately predicts train delays using machine learning algorithms
* Recommends optimal train options based on predicted delays
* Enhances passenger convenience by providing actionable insights for travel planning

---

## 🧠 Key Features

* 🔍 Delay prediction using a trained Machine Learning model
* 🚆 Train-specific predictions based on user-provided inputs
* 📊 Confidence score indicating prediction reliability
* 🟢 Delay classification (On Time / Slight Delay / High Delay)
* 🗺️ Interactive map integration for enhanced user experience
* 📅 Prediction based on journey date and temporal patterns
* ⭐ Recommendation of the best train with minimal delay

---

## 🧾 User Input

The system requires the following inputs from the user:

* Train Number
* Source Station
* Destination Station
* Journey Date

---

## 📤 Output

Based on the provided inputs, the system generates:

* Predicted Delay (in minutes)
* Confidence Score (%)
* Delay Status Classification
* Recommended Train Option

---

## 🤖 Machine Learning Model

* **Algorithm Used:** Random Forest Regressor
* **Dataset:** Indian Railway Delay Dataset (sourced from Kaggle)
* **Features Considered:**

  * Percentage of trains arriving on time
  * Percentage of slight delays
  * Percentage of significant delays
  * Percentage of cancellations
  * Day of the week (derived feature)

---

## 📊 Model Performance

The model demonstrates strong predictive performance with the following evaluation metrics:

* Mean Absolute Error (MAE): ~6 minutes
* Root Mean Squared Error (RMSE): ~13 minutes
* R² Score: ~0.91

These results indicate that the model explains approximately 91% of the variance in train delays, making it reliable for practical use.

---

## 🛠️ Tech Stack

Backend: Python (Flask Framework)
* **Frontend:** HTML, CSS, JavaScript
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Visualization & Mapping:** Leaflet.js

---

## 🌐 Live Demo

👉 https://transport-delay-project.onrender.com


---

## 🚀 Future Improvements

* Integration with real-time railway APIs for live data updates
* Development of a mobile application for wider accessibility
* Implementation of advanced models such as XGBoost or Deep Learning
* Personalized notifications and alert systems for users

---

## 📌 Conclusion

This project successfully demonstrates the application of Machine Learning in the transportation domain. By predicting train delays and providing intelligent recommendations, the system enhances passenger experience and contributes to more efficient travel planning. It highlights the potential of data-driven solutions in improving public transport reliability and decision-making processes.
