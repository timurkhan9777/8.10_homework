from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class UserVideo(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='messages/video/',validators=[
        FileExtensionValidator(allowed_extensions=['mp4','MOV','AVI','WMV'])
    ])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title