from django import forms
from . import models
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):#this form is used to edit the Profile that django already stored for you
    class Meta:
        model  = User
        fields = [
            'username','first_name','last_name','email'
        ]


class ProfileForm(forms.ModelForm):#this form is used to edit the Profile
    class Meta:
        model = models.Profile
        fields = [
            'occupation','Bio','img'
        ]
