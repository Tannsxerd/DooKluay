from django.urls import path
from .views.disease import DiseaseList
from .views.Prediction import PredictionViewSet,PredictionHistoryViewSet

# Define urlpatterns by manually specifying each path
urlpatterns = [
    # --- Endpoints for Disease (using APIView) ---

    # GET /diseases/ -> calls the DiseaseList view
    path('diseases/', DiseaseList.as_view(), name='disease-list'),

    # --- Endpoints for Prediction (using ViewSet) ---
    # We will manually map HTTP methods to view actions

    # POST /predict/ -> maps to the 'create' action of PredictionViewSet
    path('predict/', PredictionViewSet.as_view({'post': 'create'}), name='predict-create'),
    
    # GET /predictions/ -> maps to the 'list' action of PredictionHistoryViewSet
    path('predictions/', PredictionHistoryViewSet.as_view({'get': 'list'}), name='prediction-history-list'),
    
    # GET /predictions/{id}/ -> maps to the 'retrieve' action of PredictionHistoryViewSet
    path('predictions/<int:pk>/', PredictionHistoryViewSet.as_view({'get': 'retrieve'}), name='prediction-history-detail'),
]

