from django.shortcuts import render
from .models import blog
# Create your views here.
def blogs(request):
    blogs = blog.objects
    return render(request,'blogs.html',{'blogs':blogs})
