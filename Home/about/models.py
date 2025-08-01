from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    role = models.CharField(max_length=100)
    work = models.TextField(help_text="Short description of what they do")

    def __str__(self):
        return self.name
