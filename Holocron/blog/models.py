from django.db import models
from django.utils import timezone

# Create your models here.
class blogContent(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    author = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now())
    
    def __str__(self) :
        return self.name