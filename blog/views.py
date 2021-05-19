from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.
from .models import *


def main_feed(request):
    posts = Post.objects.all()   # all -> filter
    categories = Category.objects.all()
    paginator = Paginator(posts, 2)  # show 2 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'feed.html', {
        'posts': posts,
        'categories': categories,
        'page_obj': page_obj,

    })

def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        'post': post,

    })


def get_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)  # all -> filter
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)

    paginator = Paginator(posts, 2)  # show 2 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'feed.html', {
        'posts': posts,
        'categories': categories,
        'page_obj': page_obj,
        'category': category

    })









