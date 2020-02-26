from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from .models import Hall


def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self,form):
        view = super(SignUp,self).form_valid(form)
        username, password = form.cleaned_data.get('username'),form.cleaned_data.get('password1') #password1 not password
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class Create(generic.CreateView):
    model = Hall
    fields = ['title']
    success_url = reverse_lazy('home')
    template_name = 'create.html'


    def form_valid(self,form):
        form.instance.user = self.request.user
        super(Create,self).form_valid(form)
        return redirect('home')

class Detail(generic.DetailView):
    model = Hall
    template_name = 'detail.html'


class Update(generic.UpdateView):
    model = Hall
    template_name = 'update.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class Delete(generic.DeleteView):
    model = Hall
    template_name = 'delete.html'
    success_url = reverse_lazy('dashboard')
