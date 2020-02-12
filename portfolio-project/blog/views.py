from django.shortcuts import render , get_object_or_404
from .models import blog

# Create your views here.
def blogs(request):
    blogs = blog.objects
    return render(request,'blogs.html',{'blogs':blogs})
def detail(request,blog_id):
    detail_blog = get_object_or_404(blog,pk=blog_id)
    return render(request,'detail.html',{'detail_blog':detail_blog})
