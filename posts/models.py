from django.db import models



class Hashtag(models.Model):
    title = models.CharField(max_length=500)
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    likes = models.IntegerField()
    hashtags = models.ForeignKey(Hashtag, blank=True)

    def __str__(self):
        return self.title
