from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vols',views.vols, name='vols'),
    path('compagnies',views.compagnies, name='compagnies'),
    path('volsdetails/<str:pk>',views.volsdetails, name='volsdetails'),
    
]