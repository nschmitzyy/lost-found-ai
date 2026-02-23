import firebase_admin
from firebase_admin import credentials, firestore, storage
import streamlit as st
import json

if not firebase_admin._apps:
    firebase_dict = json.loads(st.secrets["FIREBASE_CREDENTIALS"])
    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred, {
        'storageBucket': st.secrets["FIREBASE_STORAGE_BUCKET"]
    })

db = firestore.client()
bucket = storage.bucket()
