from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import ImageUpload
from ..exceptions.BadRequestException import BadRequestException
from django.core.paginator import Paginator
from ..serializers.image import ImageSerializer
class ImageDetailView(APIView):
    def get(self, request, image_id,):
        image_obj = get_object_or_404(ImageUpload, pk=image_id)
        return JsonResponse({
            "id": image_obj.image_id,
            "file_path": image_obj.file_path.path,  
            "file_url": image_obj.file_path.url
        })

class ImageViewALL(APIView):
     def get(self, request): 
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 10)
        try:
            page = int(page)
            size = int(size)
        except ValueError:
            raise BadRequestException("Query parameters 'page' and 'size' must be integers.")
        
        ALLimage = ImageUpload.objects.all()
        paginator = Paginator(ALLimage, size)
        page_obj = paginator.get_page(page)

        serializer = ImageSerializer(page_obj, many=True)

        return JsonResponse({
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": size,
            "results": serializer.data
        })