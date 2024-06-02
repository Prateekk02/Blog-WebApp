from django.db import models
from django.utils import timezone

# Create your models here.
class blogContent(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='')
    author = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='blog_thumbnails/')
    like = models.IntegerField(default=0)
    report = models.IntegerField(default=0)
    comment = models.TextField(default='')
    
    def __str__(self) :
        return self.title