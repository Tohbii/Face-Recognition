def debug_prediction(image_path):
    """
    Detailed debugging to find why some images fail
    """
    # Read original image
    original = cv2.imread(image_path)
    print(f"Original image shape: {original.shape}")
    
    # Step-by-step preprocessing
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    print(f"Grayscale shape: {gray.shape}")
    
    # Save intermediate steps
    cv2.imwrite("debug_1_grayscale.jpg", gray)
    
    # Face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    print(f"Faces detected: {len(faces)}")
    
    if len(faces) == 0:
        print("NO FACE DETECTED - cascade parameters may be too strict")
        # Try with looser parameters
        faces_loose = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
        print(f"With looser params: {len(faces_loose)} faces detected")
        return None
    
    (x, y, w, h) = faces[0]
    face = gray[y:y+h, x:x+w]
    print(f"Face ROI shape: {face.shape}")
    cv2.imwrite("debug_2_face_roi.jpg", face)
    
    # Resize
    face_resized = cv2.resize(face, IMG_SIZE)
    print(f"Resized face shape: {face_resized.shape}")
    cv2.imwrite("debug_3_resized.jpg", face_resized)
    
    # Predict
    label, confidence = recognizer.predict(face_resized)
    print(f"Prediction - Label: {label}, Confidence: {confidence}")
    
    # Compare with training images
    if label in label_map:
        print(f"Matched with: {label_map[label]}")
    else:
        print(f"Unknown label: {label}")
    
    return face_resized, label, confidence