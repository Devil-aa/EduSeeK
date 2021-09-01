from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post

# Create your views here.

def interships(request):
    posts = Post.objects.all()
    return render(request, 'interships/intership.html', {
        "posts" : posts,
    })

