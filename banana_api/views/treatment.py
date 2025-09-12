from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from ..models import Treatment
from ..serializers.treatment import TreatmentSerializers
from ..exceptions.BadRequestException import BadRequestException
from django.shortcuts import get_object_or_404

class Treatmentlist(APIView):
    def get(self,request):
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 10)
        try:
            page = int(page)
            size = int(size)
        except ValueError:
            raise BadRequestException("Query parameters 'page' and 'size' must be integers.")

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
    
class TreatmentDetails(APIView):
    def get(self,request,pk):
        treatment = get_object_or_404(Treatment, pk=pk)
        serializer = TreatmentSerializers(treatment)
        return Response(serializer.data)