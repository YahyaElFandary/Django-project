from django.db import models

# Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to="image/")
    summary = models.CharField(blank=True, max_length=200)
    
