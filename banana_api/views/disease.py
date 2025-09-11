from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from ..models import Disease
from ..serializers.disease import DiseaseSerializer

class DiseaseController(APIView):
    def get(self, request):
        # query param ?page=2&size=5
        page = int(request.GET.get('page', 1))
        size = int(request.GET.get('size', 10))

        diseases = Disease.objects.all()
        paginator = Paginator(diseases, size)
        page_obj = paginator.get_page(page)

        serializer = DiseaseSerializer(page_obj, many=True)

        return Response({
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": size,
            "results": serializer.data
        })
