from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import CreateView


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
    return render(request, 'feed.html', {
        'page_obj': page_obj,
        'posts': posts,
        'page_number': page_number,
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        'post': post,
    })


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'



