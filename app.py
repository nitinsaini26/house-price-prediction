from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

print(" Starting Flask Server...")

# Load model + feature order
model = joblib.load("model.pkl")
FEATURES = joblib.load("features.pkl")

@app.route("/")
def home():
    return " House Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Extract features in correct order
        input_data = [data.get(feature, 0) for feature in FEATURES]

        features_array = np.array(input_data).reshape(1, -1)

        prediction = model.predict(features_array)

        return jsonify({
            "predicted_price": float(prediction[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# if __name__ == "__main__":
#     print(" Running Flask App...")
#     app.run(host="0.0.0.0", port=5000, debug=True)
if __name__ == "__main__":
    print(" Running Flask App...")
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
