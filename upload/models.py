from django.db import models
import uuid

class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='files/')
    capture_date = models.DateTimeField()
    capture_location = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    torchat_id = models.CharField(max_length=16)