import streamlit as st
from firebase_config import db, bucket
from services.ai_model_service import predict_image
from utils.image_utils import validate_image, open_image
from datetime import datetime

st.title("Report Found Item")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file:
    valid, error = validate_image(uploaded_file)
    
    if not valid:
        st.error(error)
    else:
        image = open_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        label, confidence = predict_image(image)

        st.write(f"Prediction: {label}")
        st.write(f"Confidence: {round(confidence * 100, 2)}%")

        if confidence > 0.7:
            blob = bucket.blob(uploaded_file.name)
            blob.upload_from_file(uploaded_file)

            db.collection("found_items").add({
                "predicted_category": label,
                "confidence": confidence,
                "image_name": uploaded_file.name,
                "status": "open",
                "created_at": datetime.utcnow()
            })

            st.success("Found item uploaded successfully!")
        else:
            st.warning("Confidence too low. Try a clearer image.")
