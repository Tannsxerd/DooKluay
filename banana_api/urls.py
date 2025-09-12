from django.urls import path
from .views.disease import DiseaseList , DiseaseDetail

urlpatterns = [
    path('disease/', DiseaseList.as_view(), name='disease_List'),# GET /api/diseases/5/ (ตัวอย่างคือดึง disease ที่มี id=5)
    path('disease/<int:pk>/', DiseaseDetail.as_view(), name='disease-detail'),
]
