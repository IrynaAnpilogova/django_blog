from django import template
from blog.models import Category, Post
from datetime import date

register = template.Library()

@register.inclusion_tag('widgetcategories.html')
def get_categories():
    categories = Category.objects.all()
    return {'categories': categories}

@register.inclusion_tag('widgetlastposts.html')
def get_last_posts(max_items=5):
    posts = Post.objects.filter(date_created__gte=date.today())[0:max_items]
    return {'posts': posts}

