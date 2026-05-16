import os
import random
import shutil

# =========================================================
# DATASET SPLITTING SCRIPT
# =========================================================
#
# PURPOSE:
# This script splits your facial recognition dataset into:
#
# 1. Training Dataset
# 2. Testing Dataset
#
# WHY?
# Machine learning models should NEVER be evaluated
# using the same images they were trained on.
#
# This script automatically:
# - reads all images,
# - shuffles them randomly,
# - splits them into train/test sets,
# - copies them into separate folders.
#
# =========================================================


# =========================================================
# CONFIGURATION
# =========================================================

# Original dataset folder
SOURCE_DATASET = "dataset"

# Output folders
TRAIN_FOLDER = "train_dataset"
TEST_FOLDER = "test_dataset"

# Train/Test ratio
TRAIN_SPLIT = 0.8   # 80% training
TEST_SPLIT = 0.2    # 20% testing


# =========================================================
# CREATE OUTPUT FOLDERS
# =========================================================

os.makedirs(TRAIN_FOLDER, exist_ok=True)
os.makedirs(TEST_FOLDER, exist_ok=True)


# =========================================================
# LOOP THROUGH EACH PERSON FOLDER
# =========================================================

for person_name in os.listdir(SOURCE_DATASET):

    person_path = os.path.join(SOURCE_DATASET, person_name)

    # Skip non-folder files
    if not os.path.isdir(person_path):
        continue

    print(f"\nProcessing: {person_name}")

    # =====================================================
    # GET ALL IMAGES
    # =====================================================

    images = []

    for image_name in os.listdir(person_path):

        if image_name.lower().endswith((".jpg", ".jpeg", ".png", ".pgm")):

            images.append(image_name)

    # =====================================================
    # SHUFFLE IMAGES RANDOMLY
    # =====================================================

    random.shuffle(images)

    # =====================================================
    # CALCULATE SPLIT INDEX
    # =====================================================

    split_index = int(len(images) * TRAIN_SPLIT)

    # =====================================================
    # SPLIT INTO TRAIN AND TEST
    # =====================================================

    train_images = images[:split_index]
    test_images = images[split_index:]

    # =====================================================
    # CREATE PERSON FOLDERS
    # =====================================================

    train_person_folder = os.path.join(TRAIN_FOLDER, person_name)
    test_person_folder = os.path.join(TEST_FOLDER, person_name)

    os.makedirs(train_person_folder, exist_ok=True)
    os.makedirs(test_person_folder, exist_ok=True)

    # =====================================================
    # COPY TRAIN IMAGES
    # =====================================================

    for image_name in train_images:

        source_path = os.path.join(person_path, image_name)

        destination_path = os.path.join(
            train_person_folder,
            image_name
        )

        shutil.copy(source_path, destination_path)

    # =====================================================
    # COPY TEST IMAGES
    # =====================================================

    for image_name in test_images:

        source_path = os.path.join(person_path, image_name)

        destination_path = os.path.join(
            test_person_folder,
            image_name
        )

        shutil.copy(source_path, destination_path)

    # =====================================================
    # PRINT RESULTS
    # =====================================================

    print(f"Training Images: {len(train_images)}")
    print(f"Testing Images : {len(test_images)}")


# =========================================================
# FINISHED
# =========================================================

print("\n===================================")
print("Dataset splitting complete!")
print("===================================")

print(f"\nTraining dataset saved to: {TRAIN_FOLDER}")
print(f"Testing dataset saved to : {TEST_FOLDER}")