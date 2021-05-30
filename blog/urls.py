
from django.urls import path
from blog.views import main_feed, get_post, get_category, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('list/', main_feed, name='home'),
    path('post/<int:post_id>/', get_post, name='post'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post')

]