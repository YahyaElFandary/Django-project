from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def wordcount(request):
    fulltext=request.GET['fulltext']
    wordsplit=fulltext.split()
    worddictionary={}
    for word in wordsplit:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    return render(request,'count.html',{'key1':fulltext,'key2':len(wordsplit),'key3':worddictionary})
