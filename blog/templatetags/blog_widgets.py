from django import template
from blog.models import Category, Post
from datetime import datetime, date


register = template.Library()

@register.inclusion_tag('widgetcategories.html')
def get_categories():
    categories = Category.objects.all()
    return {'categories': categories}

@register.inclusion_tag('widgetlastposts.html')
def get_last_posts(max_items=5):
    dt_now = datetime.now()
    filter_date = datetime(dt_now.year, dt_now.month, dt_now.day)
    posts = Post.objects.filter(date_created__gte=date.today())[0:max_items]
    return {'posts': posts}

