# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

FANTASY = 0
FICTION = 1
NON_FICTION = 2


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class Book(Base):

    class Meta:
        ordering = ('name', 'created')
        verbose_name = u'Книжка'
        verbose_name_plural = u'Книжки'

    GENRES = (
        (FANTASY, 'fantasy'),
        (FICTION, 'fiction'),
        (NON_FICTION, 'non-fiction'),
    )
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(verbose_name=u'Опис книжки')
    year = models.PositiveSmallIntegerField()
    img = models.ImageField(upload_to='books/', null=True, blank=True)
    genre = models.SmallIntegerField(choices=GENRES, default=0)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Boo(Base):
    name = models.CharField(max_length=200, db_index=True)
