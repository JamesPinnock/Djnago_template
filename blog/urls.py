from django.conf.urls import url
from django.contrib import admin
from .views import VehicleListView
from . import views


urlpatterns = [
    url('home/', VehicleListView.as_view() , name='blog-home'),
    url('about/', views.about, name='blog-about'),
]


