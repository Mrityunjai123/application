# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pF9kJneERFxP3Xo83EZ2V64ArQmg1y1b
"""

import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the models
pcos_model = tf.keras.models.load_model(r"C:\Users\Mrityunjai\Downloads\upload\upload\vgg16_pcos_detection_final.h5")
cancer_model = tf.keras.models.load_model(r"D:\SHI Project\vgg16_breast_cancer_final.h5")

# Function to preprocess the image
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize the image to 224x224 pixels
    img = image.img_to_array(img)  # Convert the image to a NumPy array
    img = np.expand_dims(img, axis=0)  # Expand dimensions to match the model's input shape
    img = img / 255.0  # Normalize the image
    return img

# Function to predict PCOS
def predict_pcos(img):
    img = preprocess_image(img)
    prediction = pcos_model.predict(img)
    if prediction[0][0] > 0.5:
        return "PCOS Detected"
    else:
        return "No PCOS Detected"

# Function to predict Breast Cancer
def predict_cancer(img):
    img = preprocess_image(img)
    prediction = cancer_model.predict(img)
    if prediction[0][0] > 0.5:
        return "Breast Cancer Detected"
    else:
        return "No Breast Cancer Detected"

# Streamlit app
st.title("PCOS and Breast Cancer Detection")

# Tab for PCOS detection
st.header("PCOS Detection")
uploaded_file_pcos = st.file_uploader("Upload an image for PCOS detection", type=["jpg", "jpeg", "png"], key="pcos")
if uploaded_file_pcos is not None:
    image_pcos = Image.open(uploaded_file_pcos)
    st.image(image_pcos, caption="Uploaded Image", use_column_width=True)
    if st.button("Predict PCOS"):
        result = predict_pcos(image_pcos)
        st.write(result)

# Tab for Breast Cancer detection
st.header("Breast Cancer Detection")
uploaded_file_cancer = st.file_uploader("Upload an image for Breast Cancer detection", type=["jpg", "jpeg", "png"], key="cancer")
if uploaded_file_cancer is not None:
    image_cancer = Image.open(uploaded_file_cancer)
    st.image(image_cancer, caption="Uploaded Image", use_column_width=True)
    if st.button("Predict Breast Cancer"):
        result = predict_cancer(image_cancer)
        st.write(result)