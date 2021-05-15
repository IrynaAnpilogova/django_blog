from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def main_feed(request):
    posts = Post.objects.all()   # all -> filter

    return render(request, 'feed.html', {
        'posts': posts
    })

def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        'post': post
    })


