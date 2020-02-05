from django.urls import include , path , re_path
from . import views  #from the same directory we are in include views


app_name='project1_app'
urlpatterns = [
    # path('projectapp', include('project1_app.urls')),
    # path('project1', include('project1_app.urls')),
    path('', views.test, name='test'), #from view import the function called test and name it test
    #path('', views.test2, name='test2'), #from view import the function called test2 and name it test2
    #re_path(r'^(?P<id>\d+)$',views.test2, name='test2')
    re_path(r'^(?P<slug>[-\w]+)/$',views.test2, name='test3'),
    re_path(r'^(?P<slug>[-\w]+)/edit',views.edit, name='edit'),
    #path('<slug:slug>', views.test2, name='test3'),
    path('add', views.note_add, name='add_note'),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#from extra elaboration: if i left my path empty path('', views.test, name='test') then it will be returned when no path
#is called(no url is called) meaning it will return function test from views
#when the url you are called doesnt call an exact function
