import os
from django.conf import settings
from rest_framework.exceptions import ValidationError, NotFound

# Models
from ..models import Disease, Prediction

# Serializers
from ..serializers import ImageUploadSerializer

# --- Machine Learning Model Logic ---
# คุณสามารถย้ายฟังก์ชันนี้มาจาก views.py หรือ import มาจากไฟล์ utils อื่นๆ
def run_prediction_model(image_path):
    """
    จำลองการทำงานของโมเดล Machine Learning กับรูปภาพ
    
    Args:
        image_path (str): Path แบบเต็มของไฟล์รูปภาพ

    Returns:
        tuple: (predicted_disease_name, confidence_score)
    """
    # =================================================================
    # TODO: นำโค้ดการทำนายผลของโมเดลจริงมาใส่แทนที่ส่วนนี้
    # =================================================================
    print(f"Simulating prediction for: {image_path}")
    # เพื่อการสาธิต จะ return ค่าคงที่กลับไป
    return ('Tomato___Late_blight', 0.987)


class PredictionService:
    """
    Service class to encapsulate the business logic for predictions.
    """
    @staticmethod
    def create_prediction_from_upload(request_data):
        """
        จัดการตรรกะหลักในการสร้าง prediction จากรูปภาพที่อัปโหลด
        1. ตรวจสอบและบันทึกรูปภาพ
        2. เรียกใช้โมเดลเพื่อทำนายผล
        3. สร้างและ return Prediction object ที่ได้
        
        Raises:
            ValidationError: หากข้อมูลที่ส่งมาไม่ถูกต้อง
            NotFound: หากไม่พบโรคที่ทำนายได้ในฐานข้อมูล
        """
        # 1. ตรวจสอบไฟล์ที่อัปโหลดด้วย serializer
        upload_serializer = ImageUploadSerializer(data=request_data)
        if not upload_serializer.is_valid():
            raise ValidationError(upload_serializer.errors)

        # 2. บันทึก instance ของรูปภาพที่อัปโหลด
        image_upload_instance = upload_serializer.save()
        image_path = os.path.join(settings.MEDIA_ROOT, image_upload_instance.image.name)

        # 3. เรียกใช้โมเดลทำนายผล
        predicted_disease_name, confidence = run_prediction_model(image_path)

        # 4. ค้นหา Disease object ที่ตรงกันในฐานข้อมูล
        try:
            disease = Disease.objects.get(name=predicted_disease_name)
        except Disease.DoesNotExist:
            # หากไม่พบโรคที่ทำนายได้ ให้ raise exception
            raise NotFound(detail=f"Predicted disease '{predicted_disease_name}' not found in the database.")

        # 5. สร้าง Prediction record ใหม่
        prediction_instance = Prediction.objects.create(
            image=image_upload_instance,
            disease=disease,
            confidence=confidence
        )

        return prediction_instance
