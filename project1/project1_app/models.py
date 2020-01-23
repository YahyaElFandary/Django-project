from django.db import models
from django.contrib.auth.models import User #importing user from this library to know who is creating this note
import datetime #importing data and time library
from django.utils.text import slugify #importing slugify
# Create your models here.

#this class is used to create the note . it contains everything that is needed to
#create a note:user, title for the note, content of the note and the date and time this note is created.
class Note(models.Model):
    #user     = models.ForeignKey(User, on_delete=True)
    title    = models.CharField(max_length = 10) #title for the note
    slug     = models.SlugField(null=True ,blank=True)#sluf
    content  = models.TextField(blank=True)# content of the note in a large text file
    created  = models.DateTimeField(blank=True, default=datetime.datetime.now)# data and time field so the user can enter the data and the time he created this note
    active   = models.BooleanField(default=True) #a checkbox to display the note or not
    tags     = models.CharField(max_length=100)#tags for the seo


    #this function is used if the user didnt enter a slug so the title is used instead to fill the slug field
    def save(self, *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Note, self).save( *args , **kwargs)

    def __str__(self):
        return self.title
