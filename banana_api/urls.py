from django.urls import path
from .views.disease import DiseaseController

urlpatterns = [
    path('disease/', DiseaseController.as_view(), name='disease_List'),
]
