from django.urls import path
from .views.disease import DiseaseList, DiseaseDetail
from .views.treatment import Treatmentlist, TreatmentDetails

urlpatterns = [
    path('disease/', DiseaseList.as_view(), name='disease_List'),
    path('treatment/',Treatmentlist.as_view(), name='treatment_list'),
    path('treatment/<int:pk>/', TreatmentDetails.as_view(), name='treatment-detail'),
    path('disease/<int:pk>/', DiseaseDetail.as_view(), name='disease-detail'),# GET /api/diseases/5/ (ตัวอย่างคือดึง disease ที่มี id=5)
]
