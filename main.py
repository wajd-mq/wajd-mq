from flask import Flask, request, jsonify

from pipeline import weather_pipeline

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "Backend Running"}

@app.route("/weather")
def weather():

    city = request.args.get("city", "Muscat")

    result = weather_pipeline(city)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)