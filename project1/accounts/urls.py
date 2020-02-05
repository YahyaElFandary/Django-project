from django.urls import include , path , re_path
from . import views
from django.contrib.auth.views import LoginView , LogoutView

#it is case sensitive so p != P
app_name='accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',views.registeration,name='register'),
    re_path(r'^(?P<slug>[-\w]+)/$',views.userprofile, name='profile'),
    re_path(r'^(?P<slug>[-\w]+)/edit$',views.edit_profile, name='editprofile'),
    re_path(r'^(?P<slug>[-\w]+)/change_pass$',views.change_password, name='change_pass'),

]
