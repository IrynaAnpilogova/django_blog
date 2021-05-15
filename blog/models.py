from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(verbose_name='Title', max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=200, blank=False, null=False)
    content = models.TextField(verbose_name='Content', blank=False, null=False)
    date_created = models.DateTimeField(verbose_name='Created data', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Updated data', auto_now=True)
    photo = models.ImageField(upload_to='media', null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE, blank=True, null=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content', blank=False, null=False)
    date_created = models.DateTimeField(verbose_name='Created data', auto_now_add=True)

    def __str__(self):
        return self.content


class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    tag_title = models.CharField(verbose_name='Tag', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.tag_title

class TagsPost(models.Model):
    class Meta:
        db_table = 'tags_post'
        verbose_name = 'Tags Post'
        verbose_name_plural = 'Tags Posts'

    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE, blank=True, null=False)
    tag_title = models.ForeignKey(Tag, verbose_name='Tag',on_delete=models.CASCADE)

    def __str__(self):
        return f'Tag for {self.post}: {self.tag_title}'