from django.conf.urls import url
from django.contrib import admin
from .views import VehicleListView, VehicleDetailView
from . import views

urlpatterns = [
    url ( 'home/', VehicleListView.as_view (), name='blog-home' ),
    url ( 'vehicle/<int:pk>/', VehicleDetailView.as_view (), name='vehicle-detail' ),
    url ( 'about/', views.about, name='blog-about' ),

]
