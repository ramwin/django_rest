# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class Test(models.Model):
    GENDER_CHOICES = (
        (-1, '未知'),
        (0, '男'),
        (1, '女'),
    )
    # user = models.OneToOneField(User)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=-1)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(User)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks')
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)
