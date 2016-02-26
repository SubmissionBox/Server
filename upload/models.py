from django.db import models

class Upload(models.Model):
    description = models.TextField()
    file = models.FileField(upload_to='files/')
    capture_date = models.DateTimeField()
    capture_location = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)