import tensorflow as tf
import numpy as np

MODEL_PATH = "models/teachable_model/keras_model.h5"
LABELS_PATH = "models/teachable_model/labels.txt"

model = tf.keras.models.load_model(MODEL_PATH)

with open(LABELS_PATH, "r") as f:
    labels = [line.strip() for line in f.readlines()]

def predict_image(image):
    image = image.resize((224, 224))
    image_array = np.asarray(image)
    normalized = (image_array.astype(np.float32) / 127.5) - 1
    data = np.expand_dims(normalized, axis=0)

    prediction = model.predict(data)
    index = np.argmax(prediction)
    confidence = float(prediction[0][index])

    return labels[index], confidence
