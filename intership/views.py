from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post

# Create your views here.

def interships(request):
    posts = Post.objects.order_by('-id')[:10]

    return render(request, "intership/intership.html", {'posts': posts
    })

