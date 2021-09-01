from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.interships, name='intership'),
]