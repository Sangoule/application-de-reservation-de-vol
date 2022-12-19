from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vols',views.vols, name='vols'),
    
]