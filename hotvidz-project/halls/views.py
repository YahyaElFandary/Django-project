from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from .models import Hall , Video
from .forms import VideoForm, SearchForm
from django.http import Http404 ,JsonResponse
import urllib
import requests
from django.forms.utils import ErrorList

<<<<<<< HEAD
YOUTUBE_API_KEY = 'AImzaoSytB_hKeekKryYfHHuLHcxJkuIeX6rBF1N_CTHmcsHC2kE'
=======
YOUTUBE_API_KEY = 'AIzaSyB_KekKyYHHLHxJuIX6BFN_CTHmcsHC2kE'
>>>>>>> ca22fe03fed481a19c9698b3ca46290a261cbe2a

def home(request):
    return render(request,'home.html')

def dashboard(request):
    halls = Hall.objects.filter(user=request.user)
    return render(request,'dashboard.html',{'halls':halls})

def addvideo(request, pk):
    form = VideoForm()
    search_form = SearchForm()
    hall = Hall.objects.get(pk=pk)
    if not hall.user == request.user:
        raise Http404
    if request.method=='POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.hall = hall
            video.url = form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id:
                video.youtube_id = video_id[0]
                response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={ YOUTUBE_API_KEY }')
                json = response.json()
                title = json['items'][0]['snippet']['title']
                video.title =title
                video.save()
                return redirect('detail',pk)
            else:
                errors = form._errors.setdefault('url',ErrorList())
                errors.append('Needs to be a YouTube URL')
    return render(request,'addvideo.html',{'form':form,'search_form':search_form,'hall':hall})

def searchVideo(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        encoded_search_term = urllib.parse.quote(search_form.cleaned_data['search_term'])
        response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={ encoded_search_term }&key={ YOUTUBE_API_KEY }')
        return JsonResponse(response.json())
    return JsonResponse({'error':'Not able to validate form'})

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


class DeleteVideo(generic.DeleteView):
    model = Video
    template_name = 'deletevideo.html'
    success_url = reverse_lazy('dashboard')


try:
    from .local_settings_views import *
except ImportError:
    pass
