import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predict_person

app = Flask(__name__)

# Enable CORS
CORS(app)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "status": "error",
            "message": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "status": "error",
            "message": "Empty filename"
        }), 400

    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        # Save uploaded image
        file.save(filepath)

        # Run prediction
        result = predict_person(filepath)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)