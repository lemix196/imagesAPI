from rest_framework import generics, permissions
from imagesAPI.models import Image
from imagesAPI.serializers import ImageSerializer

class ImageList(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        return Image.objects.all().filter(owner=self.request.user)