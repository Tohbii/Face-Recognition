import os
import pickle
import cv2
import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

from utils import preprocess_face

# Load model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model/face_model.yml")

with open("model/labels.pkl", "rb") as f:
    label_map = pickle.load(f)

TEST_PATH = "test_dataset"

y_true = []
y_pred = []

for label, person_name in label_map.items():

    person_folder = os.path.join(TEST_PATH, person_name)

    if not os.path.exists(person_folder):
        continue

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        face = preprocess_face(image_path)

        if face is None:
            continue

        pred_label, confidence = recognizer.predict(face)

        y_true.append(label)
        y_pred.append(pred_label)

# Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average="weighted")
recall = recall_score(y_true, y_pred, average="weighted")
f1 = f1_score(y_true, y_pred, average="weighted")

print("\nMODEL EVALUATION")
print("----------------------")

print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")
print(f"F1 Score : {f1:.2f}")

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

unique_labels = sorted(list(set(y_true)))

display_names = [
    label_map[label]
    for label in unique_labels
]

plt.figure(figsize=(20, 20))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=display_names
)

disp.plot(cmap=plt.cm.Blues,
          xticks_rotation=90
          )

plt.title("Confusion Matrix")

plt.show()