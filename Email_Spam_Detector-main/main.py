from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from spams import prediction

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Home route to serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle predictions
@app.route("/predict", methods=['POST'])
def predict():
    data = request.json.get("data", [])
    if data:
        prediction_result = prediction(data)
        print(prediction_result)
        print(type(prediction_result))
        return jsonify({"Result": str(prediction_result)})
    else:
        return jsonify({"Result": "No data provided"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)