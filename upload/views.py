from django.shortcuts import render

from .models import Upload

def review(request):
    upload = Upload.objects.all()
    return render(request, 'review.html', {'upload' : upload})