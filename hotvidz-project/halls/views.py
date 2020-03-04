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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

YOUTUBE_API_KEY = 'AImzaoSytB_hKeekKryYfHHuLHcxJkuIeX6rBF1N_CTHmcsHC2kE'

def home(request):
    recent_halls = Hall.objects.all().order_by('-id')[:3]
    popular_halls = [Hall.objects.get(pk=2),Hall.objects.get(pk=3),Hall.objects.get(pk=4)]
    return render(request,'home.html',{'recent_halls':recent_halls,'popular_halls':popular_halls})
@login_required
def dashboard(request):
    halls = Hall.objects.filter(user=request.user)
    return render(request,'dashboard.html',{'halls':halls})
@login_required
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
@login_required
def searchVideo(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        encoded_search_term = urllib.parse.quote(search_form.cleaned_data['search_term'])
        response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={ encoded_search_term }&key={ YOUTUBE_API_KEY }')
        return JsonResponse(response.json())
    return JsonResponse({'error':'Not able to validate form'})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'signup.html'

    def form_valid(self,form):
        view = super(SignUp,self).form_valid(form)
        username, password = form.cleaned_data.get('username'),form.cleaned_data.get('password1') #password1 not password
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class Create(LoginRequiredMixin, generic.CreateView):
    model = Hall
    fields = ['title']
    success_url = reverse_lazy('home')
    template_name = 'create.html'


    def form_valid(self,form):
        form.instance.user = self.request.user
        super(Create,self).form_valid(form)
        return redirect('dashboard')

class Detail(generic.DetailView):
    model = Hall
    template_name = 'detail.html'


class Update(LoginRequiredMixin, generic.UpdateView):
    model = Hall
    template_name = 'update.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        hall = super(Update, self).get_object()
        if not hall.user == self.request.user :
            raise Http404
        return hall

class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Hall
    template_name = 'delete.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        hall = super(Delete, self).get_object()
        if not hall.user == self.request.user :
            raise Http404
        return hall

class DeleteVideo(LoginRequiredMixin, generic.DeleteView):
    model = Video
    template_name = 'deletevideo.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        video = super(DeleteVideo, self).get_object()
        if not video.hall.user == self.request.user :
            raise Http404
        return video

try:
    from .local_settings_views import *
except ImportError:
    pass
