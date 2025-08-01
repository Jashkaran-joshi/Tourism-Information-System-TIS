from django.db import models
from datetime import date

# Create your models here.

class News(models.Model):
    CATEGORY_CHOICES = [
        ('travels', 'Travels'),
        ('organization', 'Organization'),
        ('tips', 'Tips & Tricks'),
        ('uncategorized', 'Uncategorized'),
        ('latest', 'Latest News'),
    ]

    image = models.ImageField(upload_to='news_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=date.today)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='latest')

    def __str__(self):
        return self.heading