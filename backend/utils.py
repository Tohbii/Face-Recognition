import os
import cv2
import numpy as np

# Path to Haar Cascade XML file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CASCADE_PATH = os.path.join(
    BASE_DIR,
    "haarcascade",
    "haarcascade_frontalface_default.xml"
)

# Load Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

# Standard image size for training
IMG_SIZE = (100, 100)


def preprocess_face(image_path):
    """
    This function:
    1. Reads image
    2. Converts image to grayscale
    3. Detects face
    4. Crops face
    5. Resizes face

    Why grayscale?
    ----------------
    Facial recognition focuses more on patterns and textures
    rather than colors.

    Using grayscale:
    - reduces computation
    - speeds up training
    - improves consistency

    Why resizing?
    ----------------
    All images must have same dimensions so the ML model
    learns consistent facial features.
    """

    image = cv2.imread(image_path)

    if image is None:
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale (
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # If no face detected
    if len(faces) == 0:
        return None

    # Take first detected face
    (x, y, w, h) = faces[0]

    face = gray[y:y+h, x:x+w]

    # Resize image
    face = cv2.resize(face, IMG_SIZE)

    face = cv2.equalizeHist(face)  # Optional: improve contrast

    return face


def load_dataset(dataset_path):
    """
    Loads dataset from folder structure.

    Example:
    dataset/
        John/
        Mary/

    Folder names become labels.
    """

    faces = []
    labels = []
    label_map = {}

    current_label = 0

    # Loop through each person folder
    for person_name in os.listdir(dataset_path):

        person_folder = os.path.join(dataset_path, person_name)

        if not os.path.isdir(person_folder):
            continue

        # Assign numerical label
        label_map[current_label] = person_name

        # Loop through images
        for image_name in os.listdir(person_folder):

            image_path = os.path.join(person_folder, image_name)

            face = preprocess_face(image_path)

            if face is not None:
                faces.append(face)
                labels.append(current_label)

        current_label += 1

    return faces, labels, label_map