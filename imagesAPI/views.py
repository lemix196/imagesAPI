from rest_framework import generics, permissions
from imagesAPI.models import Image
from imagesAPI.serializers import ImageSerializer
from django.shortcuts import render

class ImageList(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    # authentication - list images only for logged users
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        """Adding owner for serialized data"""
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        """Getting the queryset for view filtered by currently logged user"""
        return Image.objects.all().filter(owner=self.request.user)

    

# Image view (to improve)
def show_image(request, id):
    image = Image.objects.get(pk=id)
    user = request.user
    context = {
        'image': image,
        'user': user
    }
    if request.method == 'GET':
        return render(request, 'show_image.html', context=context)


def create_thumbnail(request, id, thumbnail_height):
    image = Image.objects.get(pk=id)
    return None
