from .models import Upload
from rest_framework import serializers

class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = ('id', 'description', 'file', 'capture_date', 'capture_location', 'upload_date', 'torchat_id')