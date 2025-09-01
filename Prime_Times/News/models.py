from django.db import models
from django.utils import timezone

# Create your models here.

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
