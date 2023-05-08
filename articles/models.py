from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to = 'images',
        processors = [Thumbnail(200,200)],
        format = 'JPEG'
    )
    image_thumb = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(90,90)],
        format = 'JPEG',
        options = {'quality':90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)