import cv2
import pickle

from utils import preprocess_face

MODEL_PATH = "model/face_model.yml"
LABELS_PATH = "model/labels.pkl"

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

# Load labels
with open(LABELS_PATH, "rb") as f:
    label_map = pickle.load(f)


def predict_person(image_path):

    face = preprocess_face(image_path)

    if face is None:
        return {
            "status": "error",
            "message": "No face detected"
        }

    # Predict
    label, confidence = recognizer.predict(face)

    """
    IMPORTANT:
    Lower confidence value = better match in OpenCV LBPH

    Example:
    20 = strong match
    80 = weak match
    """

    THRESHOLD = 60

    if confidence > THRESHOLD:
        return {
            "status": "success",
            "predicted_person": "Unknown Person",
            "confidence": round(confidence, 2)
        }

    predicted_name = label_map[label]

    return {
        "status": "success",
        "predicted_person": predicted_name,
        "confidence": round(confidence, 2)
    }