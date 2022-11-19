from django.contrib.auth.models import User
from imagesAPI.models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Image
        fields = ['id', 'img', 'original_url', 'owner']
        


class UserSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'images']