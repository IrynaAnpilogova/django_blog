
from django.urls import path
from blog.views import main_feed, get_post, AddPostView


urlpatterns = [
    path('list/', main_feed, name='home'),
    path('post/<int:post_id>/', get_post, name='get_page'),
    path('add_post/', AddPostView.as_view(), name='add_post'),

]