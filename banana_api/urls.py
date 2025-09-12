from django.urls import path
from .views.disease import DiseaseList

urlpatterns = [
    path('disease/', DiseaseList.as_view(), name='disease_List'),
]
