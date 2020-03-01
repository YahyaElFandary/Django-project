from .models import Video
from django import forms

#Model based forms
class VideoForm(forms.ModelForm):
    class Meta():
        model = Video
        fields = ['url']
        labels = {'url':'YouTube URL'}


#regular django forms
#model based forms take blank and null but regular django forms take required
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos', required=False)
