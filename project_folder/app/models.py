from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title =  models.CharField(max_length=50)
    content =  models.TextField(blank=False)
    date_posted  =  models.DateTimeField(default =  timezone.now)
    author =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comments =  models.ManyToManyField("Comment", blank =  True)
    category =  models.ManyToManyField("Category", blank = True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment =  models.CharField(max_length=200, blank =  True)
    author =  models.ForeignKey(User, null =  True, on_delete=models.CASCADE)


    def __repr__(self):
        return self.comment, self.author

    def __str__(self):
        return self.author, self.author


class Category(models.Model):
    type = models.CharField(max_length=200, blank=True)

    def __repr__(self):
        return self.type

    def __str__(self):
        return self.type

