from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    image = models.ImageField(upload_to='images/')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)