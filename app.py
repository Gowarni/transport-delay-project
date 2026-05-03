from flask import Flask, render_template, request
from integration import predict_delay
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    try:
        train_number = request.form['train_number']
        from_station = request.form['from_station']
        to_station = request.form['to_station']
        journey_date = request.form['journey_date']

        # convert date → day
        day_of_week = datetime.strptime(journey_date, "%Y-%m-%d").weekday()

        results = predict_delay(from_station, to_station, day_of_week)

        return render_template(
            "index.html",
            results=results,
            journey_date=journey_date
        )

    except Exception as e:
        print("Error:", e)
        return render_template("index.html", results=None)


if __name__ == "__main__":
    app.run(debug=True)