from django.db import models
from django.utils import timezone
import json


class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):

    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    post = models.ManyToManyField(Post)

    def __str__(self):             
        return self.name


class Comment(models.Model):

    comment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )