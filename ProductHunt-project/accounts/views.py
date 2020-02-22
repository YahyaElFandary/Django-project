from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render (request, 'signup.html',{'error':'username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request, 'signup.html',{'error':'Passwords must match!'})
    else:
        return render (request, 'signup.html')
# def signup(request):
#     if request.method =="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#
#     return render (request, 'signup.html',{'form' :form})


def login(request):
    return render(request,'login.html')

def logout(request):
    pass
