from django.urls import include , path
from . import views  #from the smae directory we are in include views

urlpatterns = [
    #path('projectapp/', include('project1_app.urls')),
    path('', views.test, name='test'), #from view import the function called test and name it test
    path('projectapp2/', views.test2, name='test2'), #from view import the function called test2 and name it test2
]
#from extra elaboration: if i left my path empty path('', views.test, name='test') then it will be returned when no path 
#is called(no url is called) meaning it will return function test from views
#when the url you are called doesnt call an exact function
