from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        "name":"name value 1",
        "textA":"text value 2",
        "textB":"text value 3"
    },
    {

        "name":"name stand",
        "textD":"text value 02 ",
        "textF":"text value 03"
    }
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': "About"})
