from django.urls import path
from .views.disease import DiseaseList, DiseaseDetail
from .views.treatment import Treatmentlist, TreatmentDetails
from .views.ImageUpload import ImageDetailView,ImageViewALL

urlpatterns = [
    # Disease endpoints
    path(
        'diseases/', 
        DiseaseList.as_view(), 
        name='disease_List'
    ),
    path(
        'diseases/<int:pk>/', 
        DiseaseDetail.as_view(), 
        name='disease-detail'
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
        'images/<int:image_id>/', 
        ImageDetailView.as_view(), 
        name='image_detail'
    ),
    path(
        'images/',
        ImageViewALL.as_view(), 
        name='all_image'
    ),
]