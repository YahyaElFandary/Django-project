from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    occupation = models.CharField(blank=True, max_length=100)
    Bio = models.TextField(blank=True)
    img = models.ImageField(upload_to="project1-img")
    Joing_date = models.DateTimeField(blank=True, default=datetime.datetime.now)



#if the slug is left empty then this functon will auto fill the slug with the entered user.if not then the entered slug can be used
    def save(self, *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile, self).save( *args , **kwargs)

    #this __str__ function will return the name of the user on the profile . as labeling
    def __str__(self):
        return '%s' %(self.user)


#create a signal
#it is used to make a profile for the user who just signed up. by clicking signup
#or submit after filling the signup page it automatically creates a profile for him
def CreateProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile =Profile.objects.create(user=kwargs['instance'])

#import post_save from django librarys
post_save.connect(CreateProfile,sender=User)
