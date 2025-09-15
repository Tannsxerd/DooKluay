from django.urls import path
from .views.disease import DiseaseList, DiseaseDetail
from .views.treatment import Treatmentlist, TreatmentDetails
from .views.ImageUpload import ImageDetailView, ImageList

urlpatterns = [
    # Disease endpoints
    path(
        'diseases/', 
        DiseaseList.as_view(), 
        name='disease_list'
    ),
    path(
        'diseases/<int:pk>/', 
        DiseaseDetail.as_view(), 
        name='disease_detail'
    ),

    # Treatment endpoints
    path(
        'treatments/',
        Treatmentlist.as_view(),
        name='treatment_list'
    ),
    path(
        'treatments/<int:pk>/', 
        TreatmentDetails.as_view(), 
        name='treatment-detail'
    ),
    
    # Image endpoints
    path(
        'images/',
        ImageList.as_view(), 
        name='image_list'
    ),
    path(
        'images/<int:pk>/', 
        ImageDetailView.as_view(), 
        name='image_detail'
    ),
]