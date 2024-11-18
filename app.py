import os
import numpy as np
from flask import Flask, request, jsonify
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import load_model

# other necessary imports

import cv2

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (assuming you have a saved model file)
MODEL_PATH = r"C:\Users\Animesh Parida\OneDrive\Desktop\iris_model\retinopathy_model.keras"
 # Replace with the actual path to your trained model
model = load_model(MODEL_PATH)

# Define image size for the model input
IMAGE_SIZE = (512, 512)

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    img_file = request.files['image']
    img_path = os.path.join('uploads', img_file.filename)
    img_file.save(img_path)

    # Preprocess the image for model prediction
    img = cv2.imread(img_path)
    img = cv2.resize(img, IMAGE_SIZE)
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Normalize the image (depending on how the model was trained)
    img = img / 255.0

    # Get prediction from the model
    prediction = model.predict(img)
    
    # Assuming the model outputs a classification score
    # Convert to severity category based on your model's output
    severity = classify_severity(prediction)

    return jsonify({"severity": severity})

def classify_severity(prediction):
    """
    Convert model output to severity classification.
    Modify this logic based on your model's actual output format.
    """
    if prediction[0] < 0.33:
        return "Mild"
    elif prediction[0] < 0.66:
        return "Moderate"
    else:
        return "Severe"

if __name__ == '__main__':
    # Ensure the uploads folder exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run(debug=True)
