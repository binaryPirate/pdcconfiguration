from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class post(models.Model):
    question=models.TextField()
    topic=models.CharField(max_length=400)
    like=models.IntegerField()
    dislike=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.question


class comments(models.Model):
    post=models.ForeignKey(post)
    text=models.TextField()
    like=models.IntegerField()
    dislike=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.post.question
