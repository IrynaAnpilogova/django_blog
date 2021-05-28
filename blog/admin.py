from django.contrib import admin

# Register your models here.

from .models import Post, Comment, Category, TagsPost, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'date_created', 'date_updated', 'is_published', 'photo')
    list_filter = ['date_created']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'parent_comment', 'content', 'date_created')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.register(Tag)
admin.site.register(TagsPost)


