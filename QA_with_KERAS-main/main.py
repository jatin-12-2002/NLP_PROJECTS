from predictionFile import Prediction
from trainQnAModel import ModelTraining

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

# Set environment variables
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Render the frontend template (index.html)
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        # Fetch form data instead of JSON
        user_story = request.form.get("story", "").split(' ')
        user_query = request.form.get("query", "").split(' ')

        if not user_story or not user_query:
            return jsonify({"error": "Invalid input. Please provide both user_story and user_query."}), 400

        predctnObj = Prediction()
        prediction = predctnObj.executeProcessing(user_story, user_query)
        
        print(prediction)
        
        return jsonify({
            'user_story': ' '.join(user_story),
            'user_query': ' '.join(user_query),
            'prediction': prediction
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)