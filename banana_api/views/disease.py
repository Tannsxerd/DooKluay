# Django imports
from django.core.paginator import Paginator
from django.http import Http404

# Third-party imports (Django REST Framework)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Local application imports
from ..exceptions.BadRequestException import BadRequestException
from ..models import Disease
from ..serializers.disease import DiseaseSerializer



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
    

# คลาสนี้ใช้สำหรับดึงข้อมูล Disease เพียงรายการเดียวตาม pk (Primary Key)
class DiseaseDetail(APIView):
    """
    ดึงข้อมูล disease จาก id ที่ระบุ
    """
    def get(self, request, pk, format=None):
        try:
            # 1. ค้นหา object จาก model Disease โดยใช้ pk ที่ได้รับจาก URL
            disease = Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            # ถ้าไม่เจอให้ raise Http404
            raise Http404("Disease not found")

        # 3. หากพบข้อมูล นำ object ไป serialize (ไม่ต้องใช้ many=True เพราะเป็น object เดียว)
        serializer = DiseaseSerializer(disease)
        
        # 4. ส่งข้อมูลที่ serialize แล้วกลับไปใน Response
        return Response(serializer.data)

