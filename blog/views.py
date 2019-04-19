from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle
from django.views.generic import ListView, DetailView

def home(request):
    context = {
        'posts': Vehicle.objects.all()
    }
    return render(request, 'blog/home.html', context)

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_added']

class VehicleDetailView(DetailView):
    model = Vehicle


def about(request):
    return render(request, 'blog/about.html',{'title': "About"})
