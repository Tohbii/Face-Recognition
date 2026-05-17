from PIL import Image
import pillow_heif
import os

# Register HEIC support
pillow_heif.register_heif_opener()

# Folder containing Jombo images
input_folder = "Jombo olatunbos..."

# Loop through all files
for filename in os.listdir(input_folder):

    # Check if file is HEIC
    if filename.lower().endswith(".heic"):

        # Full image path
        heic_path = os.path.join(input_folder, filename)

        # Open HEIC image
        image = Image.open(heic_path)

        # Create JPG filename
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"

        # Save path
        jpg_path = os.path.join(input_folder, jpg_filename)

        # Convert and save
        image.convert("RGB").save(jpg_path, "JPEG")

        print(f"Converted: {filename} -> {jpg_filename}")

print("All images converted successfully!")