from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):

    title = models.CharField(blank=False ,max_length=60)
    url = models.TextField(blank=True)
    pub_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    votes_total = models.IntegerField(blank=True, default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    body = models.TextField(blank=False)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
