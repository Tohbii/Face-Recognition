import os
import cv2
import pickle
import numpy as np

from utils import load_dataset

# Dataset path
DATASET_PATH = "dataset"

# Create LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

"""
LBPH = Local Binary Pattern Histogram

How LBPH works conceptually:
----------------------------

LBPH examines local texture patterns in the face.

It:
1. Looks at neighboring pixels
2. Creates binary patterns
3. Converts patterns into histograms
4. Compares histograms during prediction

Why LBPH is good for beginners:
--------------------------------
- Fast training
- Works well on small datasets
- Doesn't require GPU
- Good enough for academic projects
"""

print("Loading dataset...")

faces, labels, label_map = load_dataset(DATASET_PATH)

print(f"Total faces loaded: {len(faces)}")

# Convert labels to numpy array
labels = np.array(labels)

# Train recognizer
recognizer.train(faces, labels)

# Create model directory
os.makedirs("model", exist_ok=True)

# Save trained model
recognizer.save("model/face_model.yml")

# Save labels
with open("model/labels.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("Model training complete!")
print("Model saved successfully.")