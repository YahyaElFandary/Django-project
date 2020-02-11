from django.db import models
import datetime
# Create your models here.


class blog(models.Model):
    title = models.CharField(blank=True, max_length=100)
    pub_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="image/")
