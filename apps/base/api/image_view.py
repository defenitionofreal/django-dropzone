# core imports
from ..serializers import ImageSerializer
from ..models import ImageDrop

# rest framework imports
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy User View """
    serializer_class = ImageSerializer
    queryset = ImageDrop.objects.all()
