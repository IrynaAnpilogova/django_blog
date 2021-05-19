from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.
from .models import *


def main_feed(request):
    get_category_id = int(request.GET.get('category', 0))
    if get_category_id > 0:
        posts = Post.objects.filter(category_id=get_category_id)
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 2)  # show 2 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed.html',  {
        'page_obj': page_obj,
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        'post': post,
    })


# def get_category(request, category_id):
#     posts = Post.objects.filter(category_id=category_id)  # all -> filte
#     paginator = Paginator(posts, 2)  # show 2 posts per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'feed.html', {
#         'posts': posts,
#         'page_obj': page_obj,
#
#     })









