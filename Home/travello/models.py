from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.name

class Slide(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return self.title