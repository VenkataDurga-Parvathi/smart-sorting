import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("model/healthy_vs_rotten.h5")

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0][0]

    if pred > 0.5:
        label = "Rotten"
        confidence = pred * 100
    else:
        label = "Fresh"
        confidence = (1 - pred) * 100

    return label, round(confidence,2)
