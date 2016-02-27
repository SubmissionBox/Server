from django.db import models
import uuid

class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='files/')
    capture_date = models.DateTimeField(blank=True, null=True)
    capture_location = models.CharField(max_length=200, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    torchat_id = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.description[:50]