from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Note #since models and views are in the same directory, we
#are using the .models .import Note(function) from models.py
from .forms import NoteForm
# Create your views here.

#showing all notes
def test(request):  #this function asks me for a request (from the urls.py)
    #return HttpResponse('<h1>welcome fellas </h1>')
    test=Note.objects.all() #returns all the notes from the db
    context = {
        'Notekey':test     #displays anything in the html file or template. so i can relate to it in the Note.html file
    }
    return render(request,'home.html', context)

    #render. Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
#showing one note
def test2(request, slug):
    note=Note.objects.get(slug=slug)
    context={
        'onenotekey':note
    }
    return render(request, 'oneblog.html',context)
#the whole idea of views.py that is takes the urls.py request and answers(responses) by a response which is the model.py

def note_add(request):
    # form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/home')

    else:
        form = NoteForm()
    context= {
        'form': form ,
    }
    return render(request,'add.html',context)

def edit(request, slug):
    noteedit = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST ,instance = noteedit)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/home')

    else:
        form = NoteForm(instance = noteedit)
    context= {
        'form': form ,
    }
    return render(request,'edit.html',context)
