from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):

    STATUS_CHOICES = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    published = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.title
