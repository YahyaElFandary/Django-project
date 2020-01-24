from django.shortcuts import render
# Create your views here.

#showing all notes
def test(request):
    return render(request, ' welcome in django fellas',{})


#showing one #
def test2(request):
    pass
