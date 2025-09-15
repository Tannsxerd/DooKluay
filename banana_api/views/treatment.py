from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator

from ..models import Treatment
from ..serializers.treatment import TreatmentSerializers
from ..exceptions.BadRequestException import BadRequestException
from django.shortcuts import get_object_or_404
from ..utils.pagination import get_pagination_params


class TreatmentList(APIView):
    """
    GET /api/treatments/?page=<int>&size=<int>

    Query Parameters:
        - page (int, optional): Page number to retrieve. Default = 1
        - size (int, optional): Number of records per page. Default = 10
    
    Retrieves a paginated list of treatments.
    """
    def get(self,request):
        page, size = get_pagination_params(request)

        treatment_obj = Treatment.objects.all()
        paginator = Paginator(treatment_obj, size)
        page_obj = paginator.get_page(page)
        serializer = TreatmentSerializers(page_obj, many=True)

        return Response({
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": size,
            "results": serializer.data
        })
    
class TreatmentDetail(APIView):
    """
    GET /api/treatments/<pk>/

    Path Parameters:
        - pk (int, required): The ID of the treatment to retrieve.
    
    Retrieves details of a specific treatment by ID.
    """
    def get(self, request, pk):
        treatment = get_object_or_404(Treatment, pk=pk)
        serializer = TreatmentSerializers(treatment)
        return Response(serializer.data)