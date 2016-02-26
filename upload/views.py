from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UploadSerializer
from .models import Upload

def review(request):
    upload = Upload.objects.all()
    return render(request, 'review.html', {'upload' : upload})

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all().order_by('upload_date')
    serializer_class = UploadSerializer
