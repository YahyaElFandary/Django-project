from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import UserForm , ProfileForm

# Create your views here.
def home(request):
    pass


def registeration(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = UserCreationForm()

    return render (request, 'registration/register.html',{'form' :form})


def userprofile(request, slug):
    profile=get_object_or_404(Profile, slug=slug)
    return render(request,'profile.html',{'profile':profile})


def edit_profile(request, slug):
    profile=get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        User_Form =UserForm(request.POST,  instance=request.user)
        Profile_Form =ProfileForm(request.POST,request.FILES ,instance=profile)

        if User_Form.is_valid() and Profile_Form.is_valid():
            User_Form.save()
            new_profile = Profile_Form.save()
            # new_profile = Profile_Form.save(commit=False)
            # new_profile.user = request.user
            # new_profile.save()
            return redirect('/home')

    else:
        User_Form =UserForm(instance=request.user)
        Profile_Form =ProfileForm(instance=profile)

    context = {
        'User_Form' : User_Form ,
        'Profile_Form': Profile_Form
    }

    return render(request,'edit_profile.html', context)


def change_password(request, slug):
    profile=get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user,request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect ('/home')


    else:
        password_form = PasswordChangeForm(request.user)
    return render(request,'change_pass.html',{'password_form':password_form})
