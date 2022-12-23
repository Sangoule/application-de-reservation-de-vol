from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vols',views.vols, name='vols'),
    path('compagnies',views.compagnies, name='compagnies'),
    path('volsdetails/<str:id>',views.volsdetails, name='volsdetails'),
    path('trajects',views.trajects, name='trajects'),
    
]