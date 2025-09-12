from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from ..models import Disease
from ..serializers.disease import DiseaseSerializer
from ..exceptions.BadRequestException import BadRequestException

class DiseaseList(APIView):
    def get(self, request):
        
        # query param ?page=2&size=5
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 10)
        try:
            page = int(page)
            size = int(size)
        except ValueError:
            raise BadRequestException("Query parameters 'page' and 'size' must be integers.")

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
