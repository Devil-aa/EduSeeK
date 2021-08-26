from django.urls import path
from . import views

urlpatterns = [
    
    path('/intership', views.interships, name='interships'),
]