from django.db import models
from django.contrib.auth.models import User


class Hashtag(models.Model):
    title = models.CharField(max_length=500)
    posts = models.ManyToManyField('Post')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    likes = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}, {self.text}'

