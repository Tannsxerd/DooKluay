from django.urls import path
from .views.disease import DiseaseList
from .views.ImageUpload import ImageDetailView,ImageViewALL

urlpatterns = [
    path('disease/', DiseaseList.as_view(), name='disease_List'),
    path('image/<int:image_id>/', ImageDetailView.as_view(), name='image_detail'),
    path('images/',ImageViewALL.as_view(), name='all_image')
]
