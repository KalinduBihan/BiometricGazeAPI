from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = "artifacts/model_stress.pickle"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

with open(MODEL_PATH, "rb") as f:
    model_data = pickle.load(f)
    cls = model_data["cls"]

def inference_stress(data):
    id_ = data.get("id", "Unknown")
    records = data.get("data", [])
    
    if not records:
        return {"error": "No data provided"}
    
    df = pd.DataFrame(records)
    if "TEMP" not in df or "HR" not in df:
        return {"error": "Missing required fields: HR, TEMP"}
    
    TEMP = df["TEMP"].values
    if np.any((TEMP < 26) | (TEMP > 38)):
        return {"id": id_, "stress": "Temperature should be between 26 and 38"}
    
    X = df.drop(columns=["datetime"], errors='ignore').values
    P = cls.predict(X)
    avg_stress = np.sum(P) / (len(P) * 2)
    
    if avg_stress < 0.25:
        status = "Excellent"
    elif avg_stress < 0.75:
        status = "Adequate"
    else:
        status = "Needs Improvement"
    
    return {"id": id_, "stress": status, "average_stress": f"{avg_stress * 100:.2f}%"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        result = inference_stress(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# import os
# import pickle
# import pandas as pd
# import numpy as np
# from flask import Flask, request, jsonify
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)


# # Load the stress model
# def load_model():
#     with open("./artifacts/model_stress.pickle", "rb") as f:
#         data = pickle.load(f)
#         return data["cls"]


# model = load_model()


# # Predict stress level
# def predict_stress(data):
#     df = pd.DataFrame(data)

#     TEMP = df["TEMP"].values
#     if sum((TEMP < 26) | (TEMP > 38)):
#         return {"status": "failure", "message": "The temperature should be between 26 and 38"}

#     X = df.drop(columns=["datetime"]).values
#     P = model.predict(X)

#     avg_stress = np.sum(P) / (len(P) * 2)

#     if avg_stress < 0.25:
#         status = "Resilient"
#     elif avg_stress < 0.75:
#         status = "Adaptive"
#     else:
#         status = "Overwhelmed"

#     avg_stress = avg_stress * 100
#     return {
#         "status": "success",
#         "stress": status,
#         "average_stress": f"{avg_stress:.2f}%"
#     }


# # Flask endpoint for stress prediction
# @app.route('/predict_stress', methods=['POST'])
# def predict_stress_endpoint():
#     data = request.get_json()
#     if not data:
#         return jsonify({"status": "failure", "message": "No input data provided"}), 400

#     result = predict_stress(data)
#     return jsonify(result)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)