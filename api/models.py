import uuid
from django.db import models
from django.utils import timezone

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    youtube_video_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    caption = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title