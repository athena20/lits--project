# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    cardimg = models.ImageField(upload_to='news/', blank=True, null=True)
    cardtitle = models.CharField(max_length=200)
    cardtext = models.TextField()
    carddescription = models.CharField(max_length=100)

    def __str__(self):
        return self.cardtitle

class Newsinline(models.Model):
    class Meta:
        ordering = ('-time',)

    indexes = [
        models.Index(fields=['time']),
    ]
    verbose_name = 'News'
    verbose_name_plural = 'News'
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=400)

    def str(self):
        return self.title
