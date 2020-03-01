"""hotvidz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import path
from halls import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    #AUTH
    path('signup',views.SignUp.as_view(),name='signup'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    #HALLS
    path('create/',views.Create.as_view(),name='Create'),
    path('<int:pk>/',views.Detail.as_view(),name='detail'),
    path('<int:pk>/update',views.Update.as_view(),name='update'),
    path('<int:pk>/delete',views.Delete.as_view(),name='delete'),
    #Video
    path('<int:pk>/addvideo',views.addvideo,name='addvideo'),
    path('video/search',views.searchVideo,name='searchvideo'),
    path('video/<int:pk>/delete',views.DeleteVideo.as_view(),name='deletevideo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
