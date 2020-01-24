from django.shortcuts import render
from django.http import HttpResponse
from .models import Note #since models and views are in the same directory, we
#are using the .models .import Note(function) from models.py
# Create your views here.

#showing all notes
def test(request):  #this function asks me for a request (from the urls.py)
    #return HttpResponse('<h1>welcome fellas </h1>')
    test=Note.objects.all() #returns all the notes from the db
    context = {
    'Notekey':test     #displays anything in the html file or template. so i can relate to it in the Note.html file
    }
    return render(request,'Note.html', context)

    #render. Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
#showing one note
def test2(request):
    pass


#the whole idea of views.py that is takes the urls.py request and answers(responses) by a response which is the model.py
