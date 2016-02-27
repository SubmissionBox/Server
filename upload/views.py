from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from rest_framework import viewsets
import datetime

from .serializers import UploadSerializer
from .models import Upload
from .forms import UploadForm


def review(request):
    upload = Upload.objects.all()
    return render(request, 'review.html', {'upload' : upload})

def submit(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Upload(file=request.FILES['docfile'], capture_date=datetime.datetime.now())
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('upload.views.review'))
    else:
        form = UploadForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Upload.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'submit.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all().order_by('upload_date')
    serializer_class = UploadSerializer
