from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView

from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


def main_feed(request):
    posts = Post.objects.all()   # all -> filter
    categories = Category.objects.all()
    paginator = Paginator(posts, 2)  # show 2 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed.html', {
        'page_obj': page_obj,
        'categories': categories,

    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        'post': post,
    })


def get_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)  # all -> filter
    categories = Category.objects.all()
    paginator = Paginator(posts, 2)  # show 2 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed.html', {
        'categories': categories,
        'page_obj': page_obj,

    })


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'content', 'photo')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


