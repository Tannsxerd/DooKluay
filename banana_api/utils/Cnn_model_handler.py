import os
import numpy as np
from PIL import Image
import tensorflow as tf
from django.conf import settings

class CnnModelHandler:
    """
    Singleton class to load and use the CNN model.
    Ensures the model is loaded only once.
    """
    _instance = None
    model = None
    class_names = None

    # กำหนดค่าพื้นฐานของโมเดล
    MODEL_PATH = os.path.join(settings.BASE_DIR, 'banana_api', 'CnnModel', 'banana_cnn.h5')
    # *** สำคัญมาก: แก้ไขชื่อคลาสให้ตรงกับลำดับที่โมเดลของคุณเทรนมา ***
    CLASS_NAMES = [
        'Cordana', 
        'Healthy', 
        'Pestalotiopsis', 
        'Sigatoka'
        # เพิ่มเติมตามจำนวนคลาสของโมเดล
    ]
    IMAGE_SIZE = (224, 224) # ขนาดรูปภาพที่โมเดลต้องการ

    @classmethod
    def get_instance(cls):
        """Gets the single instance of this class."""
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.load_model()
        return cls._instance

    def load_model(self):
        """Loads the Keras model from the .h5 file."""
        if os.path.exists(self.MODEL_PATH):
            print(f"Loading model from: {self.MODEL_PATH}")
            self.model = tf.keras.models.load_model(self.MODEL_PATH)
            self.class_names = self.CLASS_NAMES
            print("Model loaded successfully.")
        else:
            raise FileNotFoundError(f"Model file not found at {self.MODEL_PATH}")

    def _preprocess_image(self, image_path):
        """Loads and preprocesses an image for prediction."""
        img = Image.open(image_path).convert('RGB')
        img = img.resize(self.IMAGE_SIZE)
        img_array = np.array(img)
        # Normalize the image to [0, 1] range
        img_array = img_array / 255.0
        # Expand dimensions to create a batch of 1
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, image_path):
        """
        Predicts the class of an image.

        Returns:
            tuple: (predicted_class_name, confidence_score)
        """
        if self.model is None:
            raise RuntimeError("Model is not loaded. Call load_model() first.")
        
        # 1. เตรียมรูปภาพ
        processed_image = self._preprocess_image(image_path)
        
        # 2. ทำนายผล
        predictions = self.model.predict(processed_image)
        
        # 3. แปลงผลลัพธ์
        score = np.max(predictions[0])
        class_index = np.argmax(predictions[0])
        predicted_class = self.class_names[class_index]
        
        return predicted_class, float(score)

# สร้าง instance ของ model handler ไว้ล่วงหน้าตอนที่ Django เริ่มทำงาน
# เพื่อให้โหลดโมเดลทันที ไม่ต้องรอ request แรก
model_handler_instance = CnnModelHandler.get_instance()
