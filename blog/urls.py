
from django.urls import path
from blog.views import *


urlpatterns = [
    path('list/', main_feed, name='home'),
    path('post/<int:post_id>/', get_post, name='post'),
    path('category/<int:category_id>/', get_category, name='category'),



]