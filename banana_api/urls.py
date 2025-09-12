from django.urls import path
from .views.disease import DiseaseList, DiseaseDetail
from .views.treatment import Treatmentlist, TreatmentDetails
from .views.ImageUpload import ImageDetailView,ImageViewALL

urlpatterns = [
    path('disease/', DiseaseList.as_view(), name='disease_List'),
    path('disease/<int:pk>/', DiseaseDetail.as_view(), name='disease-detail'),# GET /api/diseases/5/ (ตัวอย่างคือดึง disease ที่มี id=5)
    path('treatment/',Treatmentlist.as_view(), name='treatment_list'),
    path('treatment/<int:pk>/', TreatmentDetails.as_view(), name='treatment-detail'),
    path('image/<int:image_id>/', ImageDetailView.as_view(), name='image_detail'),
    path('images/',ImageViewALL.as_view(), name='all_image')
]